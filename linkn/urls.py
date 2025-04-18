from django.urls import path
from . import views

app_name = 'linkn'

urlpatterns = [
    path('', views.link_create, name='link_create'),
    path('create/', views.link_create, name='link_create'),  # ✅ 먼저 작성
    path('<slug:slug>/', views.redirect_short_link, name='redirect'),
]
