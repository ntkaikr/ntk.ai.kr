# weekday/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="weekday"),
    path("api/", views.api, name="weekday_api"),  # JSON API (선택)
]
