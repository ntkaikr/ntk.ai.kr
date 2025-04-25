from django.urls import path
from .views import unit_tool

app_name = 'nunit'
urlpatterns = [
    path('', unit_tool, name='tool'),
]
