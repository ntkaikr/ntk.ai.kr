from django.urls import path
from .views import exchanger_view

app_name = 'exchanger'

urlpatterns = [
    path('', exchanger_view, name='index'),
]
