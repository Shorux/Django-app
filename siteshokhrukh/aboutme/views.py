from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('Страница приложения aboutme')


def blogs(request: HttpRequest):
    return HttpResponse('<h1>Статьи</h1>')
