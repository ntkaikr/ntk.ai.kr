from django.urls import path
from .views import dday_list, dday_delete

app_name = 'ndate'
urlpatterns = [
    path('',            dday_list,   name='dday_list'),
    path('delete/<int:pk>/', dday_delete, name='dday_delete'),
]
