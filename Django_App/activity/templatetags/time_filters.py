from django import template

register = template.Library()

@register.filter
def format_duration(value):
    hours = value // 60
    minutes = value % 60
    return "{}時間{}分".format(hours, minutes)
