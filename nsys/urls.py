from django.urls import path
from .views import sys_info

app_name = 'nsys'
urlpatterns = [
    path('', sys_info, name='info'),
]
