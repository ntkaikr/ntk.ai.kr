from django.urls import path
from .views import hash_tool

app_name = 'nhash'
urlpatterns = [
    path('', hash_tool, name='tool'),
]
