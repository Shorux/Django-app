from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.urls import reverse


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелина Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Роби', 'content': 'Биография Марго Роби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True}
]


def index(request: HttpRequest):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'blogs': data_db
    }
    return render(request, 'aboutme/index.html', data)


def about(request: HttpRequest):
    data = {'title': 'О сайте'}
    return render(request, 'aboutme/about.html', data)


def show_blog(request: HttpRequest, blog_id: int):
    return HttpResponse(f'<h1>Отображение блога с id {blog_id}</h1>')


def addpage(request: HttpRequest):
    return HttpResponse('Добавление блога')


def contact(request: HttpRequest):
    return HttpResponse('Страница контактов')


def login(request: HttpRequest):
    return HttpResponse('Страница для авторизации')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
