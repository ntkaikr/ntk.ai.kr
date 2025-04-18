"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from accounts.forms import BootstrapAuthenticationForm
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools/', include('toolhub.urls')),

    # 루트 경로에서 /tools/로 리디렉트
    path('', lambda request: redirect('toolhub:tool_list')),

    path('accounts/', include('accounts.urls')),
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=BootstrapAuthenticationForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # ← GET 허용

    path('biblecheck/', include('biblecheck.urls')),

    path('common/', include('common.urls')),

]


handler404 = 'common.views.page_not_found'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)