from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # 여기가 기본 루트!
    path('public/', views.public_book_list, name='public_book_list'),  # 공개 책 보기
    path('create/', views.create_book, name='create_book'),
    path('list/', views.book_list, name='book_list'),  # 책 목록 페이지
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/read/', views.read_book, name='read_book'),  # 읽기 모드
    path('<int:book_id>/chapter/create/', views.create_chapter, name='create_chapter'),  # 챕터 추가
    path('chapter/<int:chapter_id>/section/create/', views.create_section, name='create_section'),  # 섹션 추가
    path('<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('chapter/<int:chapter_id>/edit/', views.edit_chapter, name='edit_chapter'),
    path('section/<int:section_id>/edit/', views.edit_section, name='edit_section'),
    path('section/<int:section_id>/delete/', views.delete_section, name='delete_section'),

]
