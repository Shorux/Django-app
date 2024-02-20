from django.urls import path, register_converter

from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('blog/<slug:blog_slug>/', views.show_blog, name='blog'),
    path('category/<int:cat_id>/', views.show_category, name='category')
]
