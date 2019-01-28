from django import template

register = template.Library()


@register.filter
def index(l, i):
    if l is None:
        return None
    return l[int(i)]
