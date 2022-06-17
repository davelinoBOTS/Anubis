from django import template
from django.contrib.admin.views.main import (
    PAGE_VAR
)
from django.contrib.admin.widgets import AdminTextareaWidget
from django.forms import CharField, BooleanField, ModelChoiceField, ModelMultipleChoiceField, TypedChoiceField, \
    DateField, ImageField
from django.forms.widgets import Input, CheckboxInput, Select, DateInput, FileInput, Textarea
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


@register.filter
def bots_input_lookups(field):
    if hasattr(field, 'field') and (isinstance(field.field, CharField)):
        if isinstance(field.field.widget, AdminTextareaWidget):
            if field.field.widget.attrs:
                attrs = {
                        'class': 'form-control '+field.field.widget.attrs['class'],
                        'rows': '5',
                        'language': 'pt_BR'
                    }
            else:
                attrs = {
                        'class': 'form-control ',
                        'rows': '5',
                        'language': 'pt_BR'
                    }

            field.field.widget = Textarea(attrs)
        else:
            if field.field.widget.attrs:
                if field.field.max_length:
                    attrs = {
                        'class': 'form-control ' + field.field.widget.attrs['class'],
                        'type': 'text',
                        'maxlength': field.field.max_length
                    }
                else:
                    attrs = {
                        'class': 'form-control ' + field.field.widget.attrs['class'],
                        'type': 'text'
                    }
            else:
                if field.field.max_length:
                    attrs = {
                        'class': 'form-control ',
                        'type': 'text',
                        'maxlength': field.field.max_length
                    }
                else:
                    attrs = {
                        'class': 'form-control ',
                        'type': 'text'
                    }

            field.field.widget = Input(attrs)
    elif hasattr(field, 'field') and (isinstance(field.field, BooleanField)):

        if field.field.widget.attrs:
            attrs = {
                'class': 'form-check-input align-self-end ' + field.field.widget.attrs['class'],
                'type': 'checkbox',
            }
        else:
            attrs = {
                'class': 'form-check-input align-self-end',
                'type': 'checkbox',
            }

        field.field.widget = CheckboxInput(attrs)
    elif hasattr(field, 'field') and \
            (isinstance(field.field, ModelChoiceField) or isinstance(field.field, ModelMultipleChoiceField)):
        if hasattr(field, 'field') and isinstance(field.field, ModelChoiceField):

            if field.field.widget.attrs:
                attrs = {
                    'class': 'form-control bots-select2 ' + field.field.widget.attrs['class']
                }
            else:
                attrs = {
                    'class': 'form-control bots-select2'
                }

            field.field.widget = Select(attrs, field.field.choices)
    elif hasattr(field, 'field') and (isinstance(field.field, TypedChoiceField)):

        if field.field.widget.attrs:
            attrs = {
                'class': 'form-control bots-select2' + field.field.widget.attrs['class']
            }
        else:
            attrs = {
                'class': 'form-control bots-select2'
            }

        field.field.widget = Select(attrs, field.field.choices)
    elif hasattr(field, 'field') and (isinstance(field.field, DateField)):

        if field.field.widget.attrs:
            attrs = {
                'class': 'form-control bots-date ' + field.field.widget.attrs['class']
            }
        else:
            attrs = {
                'class': 'form-control bots-date'
            }

        field.field.widget = DateInput(attrs)
    elif hasattr(field, 'field') and (isinstance(field.field, ImageField)):

        if field.field.widget.attrs and hasattr(field.field.widget.attrs, 'class'):
            attrs = {
                'class': 'form-control custom-file bots-image-file ' + field.field.widget.attrs['class'],
                'type': 'file'
            }
        else:
            attrs = {
                'class': 'form-control custom-file bots-image-file',
                'type': 'file'
            }

        field.field.widget = FileInput(attrs)

    return field
