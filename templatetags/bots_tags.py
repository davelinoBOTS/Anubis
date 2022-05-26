from django import template
from django.contrib.admin.views.main import (
    PAGE_VAR
)
from django.template.loader import get_template
from django.utils.html import format_html

from Anubis.utils_menu import get_menu_items

register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag


########################################################################################################################
# Utilizando o código do Django JET                                                                                    #
# https://github.com/geex-arts/django-jet                                                                              #
########################################################################################################################
@assignment_tag(takes_context=True)
def bots_get_menu(context):
    return get_menu_items(context)


@register.simple_tag
def bots_paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == cl.paginator.ELLIPSIS:
        return format_html("{} ", cl.paginator.ELLIPSIS)
    elif i == cl.page_num:
        return format_html(
            '<li class="paginate_button page-item active">' +
            '<a href="{}" aria-controls="result_list" data-dt-idx="1" tabindex="0" class="page-link">{}</a>' +
            '</li>',
            cl.get_query_string({PAGE_VAR: i}),
            i
        )
    else:
        return format_html(
            '<li class="paginate_button page-item">' +
            '<a href="{}" aria-controls="result_list" data-dt-idx="1" tabindex="0" class="page-link">{}</a>' +
            '</li>',
            cl.get_query_string({PAGE_VAR: i}),
            i,
        )


@register.simple_tag
def bots_paginator_previous(cl):
    if cl.page_num > 1:
        return format_html(
            '<li class="paginate_button page-item previous">' +
            '<a href="?p={}" aria-controls="result_list" data-dt-idx="0" tabindex="0" class="page-link">' +
            'Anterior' +
            '</a>' +
            '</li>',
            cl.page_num - 1
        )
    else:
        return format_html(
            '<li class="paginate_button page-item previous disabled">' +
            '<a href="?p={}" aria-controls="result_list" data-dt-idx="0" tabindex="0" class="page-link">' +
            'Anterior' +
            '</a>' +
            '</li>',
            cl.page_num - 1
        )


@register.simple_tag
def bots_paginator_next(cl):
    if cl.page_num == cl.paginator.num_pages:
        return format_html(
            '<li class="paginate_button page-item previous disabled">' +
            '<a href="?p={}" aria-controls="result_list" data-dt-idx="0" tabindex="0" class="page-link">' +
            'Próximo' +
            '</a>' +
            '</li>',
            cl.page_num + 1
        )
    else:
        return format_html(
            '<li class="paginate_button page-item previous">' +
            '<a href="?p={}" aria-controls="result_list" data-dt-idx="0" tabindex="0" class="page-link">' +
            'Próximo' +
            '</a>' +
            '</li>',
            cl.page_num + 1
        )


@register.simple_tag
def bots_admin_list_filter(cl, spec):
    tpl = get_template(spec.template)
    return tpl.render(
        {
            "title": spec.title,
            "choices": list(spec.choices(cl)),
            "spec": spec,
        }
    )
