from django.urls import path, re_path
from . import views

app_name = 'carded'

urlpatterns = [
    path('me/', views.my_card_view, name='my_card'),
    path('delete/<int:link_id>/', views.delete_social_link, name='delete_link'),
    re_path(r'^(?P<username>(?!me$|delete$)[\w.@+-]+)/$', views.public_card_by_username, name='public_card_by_username'),
]
