from django.urls import path
from . import views

app_name = 'visitorstats'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
