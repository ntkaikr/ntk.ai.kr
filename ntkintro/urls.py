from django.urls import path
from . import views

app_name = 'ntkintro'

urlpatterns = [
    path('', views.intro_page, name='intro_page'),
]
