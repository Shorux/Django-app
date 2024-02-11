from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request: HttpRequest):
    return HttpResponse('Страница приложения aboutme')


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
