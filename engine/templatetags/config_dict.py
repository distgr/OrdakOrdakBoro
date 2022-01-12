from ordakordakboro.settings import CONFIG_DIR
from django import template

register = template.Library()

@register.simple_tag()
def get_config(value):
    return CONFIG_DIR[value] if value in CONFIG_DIR else ''