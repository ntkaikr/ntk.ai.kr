from django.urls import path
from . import views

app_name = 'agecalc'

urlpatterns = [
    path('',           views.index,     name='index'),         # 홈 (현재 나이 계산)
    path('calculate/', views.calculate, name='calculate'),     # 홈 폼 제출

    # 확장 기능들
    path('future/',     views.future,     name='future'),       # 특정 연도에 몇 살
    path('goal/',       views.goal,       name='goal'),         # 특정 나이가 되는 해
    path('birthday/',   views.birthday,   name='birthday'),     # 생일 지남 여부 계산
    path('convert/',    views.convert,    name='convert'),      # 한국 ↔ 만 나이 변환
    path('difference/', views.difference, name='difference'),  # 두 사람 나이 차이
    path('sincebirth/', views.sincebirth, name='sincebirth'),   # 출생 이후 경과일 계산
]
