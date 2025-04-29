# centurycalc/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # GET  https://www.ntk.ai.kr/centurycalc/
    path('', views.index, name='index'),
    # POST https://www.ntk.ai.kr/centurycalc/calculate/
    path('calculate/', views.calculate, name='calculate'),
]
