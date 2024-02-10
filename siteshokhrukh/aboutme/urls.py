import views

from django.urls import path

urlpatterns = [
    path('admin/'),
    path('', views.index)
]
