from django import template

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
