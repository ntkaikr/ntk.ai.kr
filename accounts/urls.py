from django.urls import path
from .views import signup
# config/urls.py 또는 views.py
from django.contrib.auth.views import LoginView
from accounts.forms import BootstrapAuthenticationForm

urlpatterns = [
    path('login/', LoginView.as_view(
        authentication_form=BootstrapAuthenticationForm,
        template_name='registration/login.html'
    ), name='login'),

    path('signup/', signup, name='signup'),
]
