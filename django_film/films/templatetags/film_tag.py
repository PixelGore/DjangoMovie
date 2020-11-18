# Imports
from django import template
# Local imports
from films.models import Category, Film


register = template.Library()


@register.simple_tag()
def get_categories():
    '''Returns all categries'''
    return Category.objects.all()

@register.inclusion_tag('films/tags/last_films.html')
def get_last_films(count=5):
    '''Return last added films'''
    films = Film.objects.order_by("id")[:count]
    return {"last_films": films}
