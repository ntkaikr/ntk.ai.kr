from django.urls import path
from . import views

app_name = 'biblecheck_youth'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.chapter_list, name='chapter_list'),
    path('book/<int:book_id>/check/', views.check_chapter, name='check_chapter'),
    path('today/', views.today_checked, name='today_checked'),  # ✅ 추가
    path('history/', views.history_checked, name='history_checked'),  # ✅ 추가


]
