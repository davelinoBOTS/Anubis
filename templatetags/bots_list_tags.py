import re

from django import template

register = template.Library()


@register.simple_tag
def bots_get_id_item_list(item):
    try:
        id_item = re.search('value="(.+?)" class', item).group(1)

        return id_item
    except AttributeError:
        pass
