from django.urls import path
from . import views

app_name = 'carded'

urlpatterns = [
    path('me/', views.my_card_view, name='my_card'),
    path('', views.card_view, name='public_card'),  # ✅ 공개용 카드 뷰
    path('<str:username>/', views.public_card_by_username, name='public_card_by_username'),  # ← 추가
    path('delete/<int:link_id>/', views.delete_social_link, name='delete_link'),
]
