from django.urls import path
from . import views

app_name = 'carded'

urlpatterns = [
    path('me/', views.my_card_view, name='my_card'),
]
