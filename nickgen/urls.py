# apps/nickgen/urls.py
from django.urls import path
from . import views


app_name = 'nickgen'


urlpatterns = [
    path('', views.generator_view, name='generator'),
    path('save/', views.save_nickname, name='save'),
    path('copy/', views.copy_ping, name='copy_ping'),
    path('api/', views.api_generate, name='api'),
]