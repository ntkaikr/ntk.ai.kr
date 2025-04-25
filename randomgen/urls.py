from django.urls import path
from .views import random_generator

app_name = 'randomgen'
urlpatterns = [
    path('', random_generator, name='generator'),
]
