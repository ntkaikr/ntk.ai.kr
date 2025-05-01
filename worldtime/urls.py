from django.urls import path
from . import views

app_name = 'worldtime'

urlpatterns = [
    path('', views.index, name='index'),
]
