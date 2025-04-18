from django.urls import path
from . import views

app_name = 'linkn'

urlpatterns = [
    path('', views.link_create, name='link_create'),
    path('<slug:slug>/', views.redirect_short_link, name='redirect'),
]
