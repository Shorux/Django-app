import aboutme.views as views

from django.template import Library

from aboutme.models import Category

register = Library()


@register.simple_tag()
def get_menu():
    return views.menu


@register.inclusion_tag('aboutme/list_categories.html')
def show_categories(cat_selected=0):
    return {'categories': Category.objects.all(), 'cat_selected': cat_selected}
