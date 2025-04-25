from django.urls import path
from .views import averaging_calculator

app_name = 'averager'
urlpatterns = [
    path('', averaging_calculator, name='calculator'),
]
