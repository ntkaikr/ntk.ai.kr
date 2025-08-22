# dailyq/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dailyq_index"),
    path("history/", views.history, name="dailyq_history"),
    path("api/today/", views.api_today, name="dailyq_api_today"),  # 선택: JSON
]
