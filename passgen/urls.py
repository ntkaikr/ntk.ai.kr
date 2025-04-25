from django.urls import path
from .views import password_generator

app_name = 'passgen'
urlpatterns = [
    path('', password_generator, name='generate'),
]
