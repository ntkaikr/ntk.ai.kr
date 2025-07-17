from django.urls import path
from . import views

app_name = 'scripter'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_script, name='create_script'),  # 추가
    path('<int:script_id>/setup/', views.setup_script, name='setup_script'),
    path('<int:script_id>/add_scene/', views.add_scene, name='add_scene'),
    path('<int:script_id>/scene/<int:scene_id>/write/', views.write_scene, name='write_scene'),
    path('my/', views.my_scripts, name='my_scripts'),

]
