from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.profile_intro, name='intro'),         # 소개 페이지
    path('view/', views.profile_view, name='view'),      # 실제 프로필 실행
]
