# agecalc/urls.py

from django.urls import path
from . import views

app_name = 'agecalc'   # <--- 추가

urlpatterns = [
    path('',           views.index,     name='index'),
    path('calculate/', views.calculate, name='calculate'),
]
