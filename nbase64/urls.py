from django.urls import path
from .views import base64_tool

app_name = 'nbase64'
urlpatterns = [
    path('', base64_tool, name='tool'),
]
