# pomodoro/urls.py
from django.urls import path
from . import views

app_name = 'pomodoro'
urlpatterns = [
    path('', views.timer, name='timer'),
    path('record/', views.record, name='record'),
]
