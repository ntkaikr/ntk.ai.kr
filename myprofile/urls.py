from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.profile_intro, name='intro'),         # 소개 페이지
    path('view/', views.profile_view, name='view'),      # 실제 프로필 실행
    path('todo/add/', views.add_todo, name='add_todo'),
    path('todo/toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('add-frequent-tool/', views.add_frequent_tool, name='add_frequent_tool'),

]
