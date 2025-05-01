# idgen/urls.py
from django.urls import path
from . import views

app_name = 'idgen'
urlpatterns = [
    path('', views.index, name='index'),
]
