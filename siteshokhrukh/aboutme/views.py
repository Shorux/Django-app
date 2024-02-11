from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('Страница приложения aboutme')


def blogs(request: HttpRequest, blog_id: int):
    return HttpResponse(f'<h1>Статья</h1><p>id: {blog_id}</p>')


def archive(request: HttpRequest, year: int):
    if year > 2024:
        raise Http404()

    return HttpResponse(f'<h1>Архив из {year} года</h1>')


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
