from django import template

register = template.Library()

@register.filter(mame='addClass')
def addClass(value, css):
    return value.as_widget(attrs={'class': css})

