from django.urls import path
from .views import info

app_name = 'nip'
urlpatterns = [
    path('', info, name='info'),
]
