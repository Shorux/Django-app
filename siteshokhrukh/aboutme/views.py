from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Women, Category, TagBlog

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(request: HttpRequest):
    blogs = Women.published.all()

    data = {
        'title': 'Главная страница',
        'blogs': blogs,
        'cat_selected': 0
    }

    return render(request, 'aboutme/index.html', data)


def about(request: HttpRequest):
    return render(request, 'aboutme/about.html', {'title': 'О сайте', 'menu': menu})


def show_blog(request: HttpRequest, blog_slug: str):
    blog = get_object_or_404(Women, slug=blog_slug)

    data = {
        'title': blog.title,
        'blog': blog,
        'cat_selected': 1
    }
    return render(request, 'aboutme/blog.html', data)


def addpage(request: HttpRequest):
    return HttpResponse("Добавление статьи")


def contact(request: HttpRequest):
    return HttpResponse("Обратная связь")


def login(request: HttpRequest):
    return HttpResponse("Авторизация")


def show_category(request: HttpRequest, cat_slug: str):
    category = get_object_or_404(Category, slug=cat_slug)
    blogs = Women.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'blogs': blogs,
        'cat_selected': category.pk
    }

    return render(request, 'aboutme/index.html', data)


def show_tag_bloglist(request: HttpRequest, tag_slug: str):
    tag = get_object_or_404(TagBlog, slug=tag_slug)
    blogs = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'blogs': blogs,
        'cat_selected': None
    }

    return render(request, 'aboutme/index.html', data)


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
