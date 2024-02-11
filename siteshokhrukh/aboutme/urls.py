from django.urls import path, register_converter

from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs/<int:blog_id>/', views.blogs_by_id, name='blog_id'),
    path('blogs/<slug:blog_slug>/', views.blogs_by_slug, name='blog_slug'),
    path('archive/<year4:year>/', views.archive, name='archive')
]
