from django.urls import path
from . import views

app_name = 'carded'

urlpatterns = [
    path('me/', views.my_card_view, name='my_card'),
    path('delete/<int:link_id>/', views.delete_social_link, name='delete_link'),
    path('', views.card_view, name='public_card'),  # /carded/ 접속 시 → 내 명함 리다이렉트
    path('<str:username>/', views.public_card_by_username, name='public_card_by_username'),
]
