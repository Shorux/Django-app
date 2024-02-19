from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render, redirect

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
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
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0
    }
    return render(request, 'aboutme/index.html', data)


def about(request: HttpRequest):
    return render(request, 'aboutme/about.html', {'title': 'О сайте', 'menu': menu})


def show_blog(request: HttpRequest, blog_id: int):
    return HttpResponse(f"Отображение статьи с id = {blog_id}")


def addpage(request: HttpRequest):
    return HttpResponse("Добавление статьи")


def contact(request: HttpRequest):
    return HttpResponse("Обратная связь")


def login(request: HttpRequest):
    return HttpResponse("Авторизация")


def show_category(request: HttpRequest, cat_id: int):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id
    }
    return render(request, 'aboutme/index.html', data)


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
