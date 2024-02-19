import aboutme.views as views

from django.template import Library

register = Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('aboutme/list_categories.html')
def show_categories(cat_selected=0):
    return {'categories': views.cats_db, 'cat_selected': cat_selected}
