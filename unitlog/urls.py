from django.urls import path
from . import views

app_name = "unitlog"

urlpatterns = [
    path("", views.residence_list, name="residence_list"),
    path("add/", views.residence_add, name="residence_add"),
]
