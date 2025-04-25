from django.urls import path
from .views import generate

app_name = 'nlorem'
urlpatterns = [
    path('', generate, name='generate'),
]
