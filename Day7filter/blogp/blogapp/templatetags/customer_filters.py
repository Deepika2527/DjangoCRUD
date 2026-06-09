from django import template

register = template.Library()

@register.filter
def trending(value):
    if value>10000:
        return "🔥 trending"
    return "Normal Views"