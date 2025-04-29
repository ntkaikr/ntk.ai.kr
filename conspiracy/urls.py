# conspiracy/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # GET  https://www.ntk.ai.kr/conspiracy/
    path('', views.post_list, name='list'),
    # GET  https://www.ntk.ai.kr/conspiracy/new/
    # POST 새 글 작성
    path('new/', views.post_create, name='create'),
    # GET  https://www.ntk.ai.kr/conspiracy/<pk>/
    path('<int:pk>/', views.post_detail, name='detail'),
    # GET/POST 편집
    path('<int:pk>/edit/', views.post_edit, name='edit'),
    # GET/POST 삭제
    path('<int:pk>/delete/', views.post_delete, name='delete'),
]
