from django.urls import path
from . import views
from .views import tool_create

app_name = 'toolhub'

urlpatterns = [
    path('', views.tool_list, name='tool_list'),
    path('<int:pk>/', views.tool_detail, name='tool_detail'),
    path('create/', tool_create, name='tool_create'),
    path('comments/<int:comment_id>/like/', views.toggle_comment_like, name='toggle_comment_like'),
    path('<int:pk>/like/', views.toggle_tool_like, name='toggle_tool_like'),
    path('<int:pk>/run/', views.run_tool, name='run_tool'),

]
