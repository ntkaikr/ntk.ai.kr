from django.urls import path
from . import views

app_name = 'biblecheck'

urlpatterns = [
    path('', views.index, name='index'),         # /biblecheck/ → 리디렉트
    path('check/', views.check, name='check'),   # /biblecheck/check/ → 템플릿 렌더
    path('history/', views.history, name='history'),
]
