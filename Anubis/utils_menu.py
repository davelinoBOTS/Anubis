from collections import OrderedDict

from django.contrib import admin
from django.contrib.admin import AdminSite

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps  # Fix Django 1.7 import issue
    except ImportError:
        pass
try:
    from django.urls import reverse, NoReverseMatch, resolve
except ImportError:  # Django 1.11
    try:
        from django.urls import reverse, NoReverseMatch, resolve
    except ImportError:
        pass

from django.utils.text import slugify, capfirst
from django.utils.translation import gettext_lazy as _

from Anubis import settings


########################################################################################################################
# Utilizando o código do Django JET                                                                                    #
# https://github.com/geex-arts/django-jet                                                                              #
########################################################################################################################
def get_menu_items(context):
    original_app_list = OrderedDict(map(lambda app: (app['app_label'], app), get_original_menu_items(context)))
    custom_app_list = settings.BOTS_MENU_CUSTOM

    if custom_app_list not in (None, False):
        if isinstance(custom_app_list, dict):
            admin_site = get_admin_site(context)
            custom_app_list = custom_app_list.get(admin_site.name, [])

        app_list = []

        def get_menu_item_app_model(app_label, data):
            item = {'has_perms': True}

            if 'name' in data:
                parts = data['name'].split('.', 2)

                if len(parts) > 1:
                    app_label, name = parts
                else:
                    name = data['name']

                if app_label in original_app_list:
                    models = dict(map(
                        lambda x: (x['name'], x),
                        original_app_list[app_label]['models']
                    ))

                    if name in models:
                        item = models[name].copy()

            if 'label' in data:
                item['label'] = data['label']

            if 'url' in data:
                item['url'] = get_menu_item_url(data['url'], original_app_list)

            if 'url_blank' in data:
                item['url_blank'] = data['url_blank']

            if 'icon' in data:
                item['icon'] = data['icon']

            if 'permissions' in data:
                item['has_perms'] = item.get('has_perms', True) and context['user'].has_perms(data['permissions'])

            return item

        def get_menu_item_app(data):
            app_label = data.get('app_label')

            if not app_label:
                if 'label' not in data:
                    raise Exception('Custom menu items should at least have \'label\' or \'app_label\' key')
                app_label = 'custom_%s' % slugify(data['label'], allow_unicode=True)

            if app_label in original_app_list:
                item = original_app_list[app_label].copy()
            else:
                item = {'app_label': app_label, 'has_perms': True}

            if 'label' in data:
                item['label'] = data['label']

            if 'items' in data:
                item['items'] = list(map(lambda x: get_menu_item_app_model(app_label, x), data['items']))

            if 'url' in data:
                item['url'] = get_menu_item_url(data['url'], original_app_list)

            if 'icon' in data:
                item['icon'] = data['icon']

            if 'url_blank' in data:
                item['url_blank'] = data['url_blank']

            if 'permissions' in data:
                item['has_perms'] = item.get('has_perms', True) and context['user'].has_perms(data['permissions'])

            return item

        for data in custom_app_list:
            item = get_menu_item_app(data)
            app_list.append(item)
    else:
        def map_item(item):
            item['items'] = item['models']
            return item

        app_list = list(map(map_item, original_app_list.values()))

    current_found = False

    for app in app_list:
        if not current_found:
            for model in app['items']:
                if not current_found and model.get('url') and context['request'].path.startswith(model['url']):
                    model['current'] = True
                    current_found = True
                else:
                    model['current'] = False

            if not current_found and app.get('url') and context['request'].path.startswith(app['url']):
                app['current'] = True
                current_found = True
            else:
                app['current'] = False

    return app_list


########################################################################################################################
# Utilizando o código do Django JET                                                                                    #
# https://github.com/geex-arts/django-jet                                                                              #
########################################################################################################################
def get_original_menu_items(context):
    original_app_list = get_app_list(context)

    return map(lambda app: {
        'app_label': app['app_label'],
        'url': app['app_url'],
        'icon': app['icon'],
        'url_blank': False,
        'label': app.get('name', capfirst(_(app['app_label']))),
        'has_perms': app.get('has_module_perms', False),
        'models': list(map(lambda model: {
            'url': model.get('admin_url'),
            'url_blank': False,
            'name': model['model_name'],
            'object_name': model['object_name'],
            'label': model.get('name', model['object_name']),
            'has_perms': any(model.get('perms', {}).values()),
        }, app['models'])),
        'custom': False
    }, original_app_list)


########################################################################################################################
# Utilizando o código do Django JET                                                                                    #
# https://github.com/geex-arts/django-jet                                                                              #
########################################################################################################################
def get_app_list(context, order=True):
    admin_site = get_admin_site(context)
    request = context['request']

    app_dict = {}
    for model, model_admin in admin_site._registry.items():
        app_label = model._meta.app_label
        try:
            has_module_perms = model_admin.has_module_permission(request)
        except AttributeError:
            has_module_perms = request.user.has_module_perms(app_label)  # Fix Django < 1.8 issue

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                    'model_name': model._meta.model_name,
                }

                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    try:
                        name = apps.get_app_config(app_label).verbose_name
                    except NameError:
                        name = app_label.title()

                    try:
                        icon = apps.get_app_config(app_label).icon
                    except AttributeError:
                        icon = 'fa-solid fa-house-laptop'
                    app_dict[app_label] = {
                        'name': name,
                        'app_label': app_label,
                        'icon': icon,
                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=admin_site.name,
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # Sort the apps alphabetically.
    app_list = list(app_dict.values())

    if order:
        app_list.sort(key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

    return app_list


########################################################################################################################
# Utilizando o código do Django JET                                                                                    #
# https://github.com/geex-arts/django-jet                                                                              #
########################################################################################################################
def get_admin_site(context):
    try:
        current_resolver = resolve(context.get('request').path)
        index_resolver = resolve(reverse('%s:index' % current_resolver.namespaces[0]))

        if hasattr(index_resolver.func, 'admin_site'):
            return index_resolver.func.admin_site

        for func_closure in index_resolver.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass

    return admin.site


########################################################################################################################
# Utilizando o código do Django JET                                                                                    #
# https://github.com/geex-arts/django-jet                                                                              #
########################################################################################################################
def get_menu_item_url(url, original_app_list):
    if isinstance(url, dict):
        url_type = url.get('type')

        if url_type == 'app':
            return original_app_list[url['app_label']]['url']
        elif url_type == 'model':
            models = dict(map(
                lambda x: (x['name'], x['url']),
                original_app_list[url['app_label']]['models']
            ))
            return models[url['model']]
        elif url_type == 'reverse':
            return reverse(url['name'], args=url.get('args'), kwargs=url.get('kwargs'))
    elif isinstance(url, str):
        return url
