from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.urls import reverse


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелина Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Роби', 'content': 'Биография Марго Роби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True}
]


def index(request: HttpRequest):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'aboutme/index.html', data)


def about(request: HttpRequest):
    data = {'title': 'О сайте'}
    return render(request, 'aboutme/about.html', data)


def blogs_by_id(request: HttpRequest, blog_id: int):
    return HttpResponse(f'<h1>Статья</h1><p>id: {blog_id}</p>')


def blogs_by_slug(request: HttpRequest, blog_slug: int):
    return HttpResponse(f'<h1>Статья</h1><p>slug: {blog_slug}</p>')


def archive(request: HttpRequest, year: int):
    if year > 2024:
        uri = reverse('blog_slug', args=('music', ))
        return redirect(uri)  # permanent=True for 301 else 302

    return HttpResponse(f'<h1>Архив из {year} года</h1>')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
