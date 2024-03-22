import aboutme.views as views

from django.template import Library
from django.db.models import Count

from aboutme.models import Category, TagBlog

register = Library()


@register.inclusion_tag('aboutme/menu.html')
def show_menu():
    return {'menu': views.menu}


@register.inclusion_tag('aboutme/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('women')).filter(total__gt=0)
    return {'categories': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('aboutme/list_tags.html')
def show_tags():
    return {'tags': TagBlog.objects.all()}
