from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import Women

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'}
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


def show_category(request: HttpRequest, cat_id: int):
    data = {
        'title': 'Главная страница',
        'posts': data_db,
        'cat_selected': cat_id
    }
    return render(request, 'aboutme/index.html', data)


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
