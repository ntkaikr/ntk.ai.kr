# bmicalc/urls.py
from django.urls import path
from . import views

app_name = 'bmicalc'
urlpatterns = [
    path('', views.index, name='index'),
]
