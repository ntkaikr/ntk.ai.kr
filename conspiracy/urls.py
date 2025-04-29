# conspiracy/urls.py
from django.urls import path
from . import views

app_name = 'conspiracy'    # ← 이 줄을 최상단에 추가!

urlpatterns = [
     path('',               views.post_list,   name='list'),
     path('new/',           views.post_create, name='create'),
     path('<int:pk>/',      views.post_detail, name='detail'),
     path('<int:pk>/edit/', views.post_edit,   name='edit'),
     path('<int:pk>/delete/', views.post_delete, name='delete'),

     # 댓글 작성
     path('<int:pk>/comment/', views.add_comment, name='add_comment'),
     # 대댓글 작성
     path('comment/<int:cid>/reply/', views.add_reply, name='add_reply'),

]
