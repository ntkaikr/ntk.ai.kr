# centurycalc/urls.py

from django.urls import path
from . import views

app_name = 'centurycalc'   # <--- 추가

urlpatterns = [
    path('',           views.index,     name='index'),
    path('calculate/', views.calculate, name='calculate'),
]
