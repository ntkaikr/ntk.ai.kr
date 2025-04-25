from django.urls import path
from .views import count

app_name = 'nword'
urlpatterns = [
    path('', count, name='count'),
]
