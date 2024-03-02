import aboutme.views as views

from django.template import Library

from aboutme.models import Category, TagBlog

register = Library()


@register.inclusion_tag('aboutme/menu.html')
def show_menu():
    return {'menu': views.menu}


@register.inclusion_tag('aboutme/list_categories.html')
def show_categories(cat_selected=0):
    return {'categories': Category.objects.all(), 'cat_selected': cat_selected}


@register.inclusion_tag('aboutme/list_tags.html')
def show_tags():
    return {'tags': TagBlog.objects.all()}
