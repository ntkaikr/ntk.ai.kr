# agecalc/urls.py

from django.urls import path
from . import views

app_name = 'agecalc'   # URL 리버스를 쓸 때 유용하지만, include 시에는 namespace 생략 가능

urlpatterns = [
    path('',          views.index,     name='index'),    # GET  /agecalc/
    path('calculate/', views.calculate, name='calculate'),# POST /agecalc/calculate/
]
