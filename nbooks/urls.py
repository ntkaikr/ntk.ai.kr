from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('list/', views.book_list, name='book_list'),  # 책 목록 페이지
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/chapter/create/', views.create_chapter, name='create_chapter'),  # 챕터 추가
    path('chapter/<int:chapter_id>/section/create/', views.create_section, name='create_section'),  # 섹션 추가

]
