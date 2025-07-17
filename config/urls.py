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
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from accounts.forms import BootstrapAuthenticationForm
from django.contrib.auth.views import LoginView
from linkn.views import redirect_short_link



urlpatterns = [

    #path('accounts/', include('allauth.urls')),  # ✅ 이거 추가

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

    path('ntkintro/', include('ntkintro.urls')),

    path('youth/', include('biblecheck_youth.urls')),


    path('linkn/', include('linkn.urls')),

    path('myprofile/', include('myprofile.urls')),

    path('carded/', include('carded.urls')),

    path('random/', include('randomgen.urls')),
    path('averager/', include('averager.urls')),
    path('passgen/', include('passgen.urls')),
    path('ndate/', include('ndate.urls')),
    path('nip/',   include('nip.urls')),
    path('nlorem/',include('nlorem.urls')),
    path('nword/', include('nword.urls')),

    path('nsys/', include('nsys.urls')),
    path('nbase64/', include('nbase64.urls')),
    path('nunit/', include('nunit.urls')),
    path('nhash/', include('nhash.urls')),
    path('nbooks/', include('nbooks.urls')),

    # 툴허브 전체 대신, 각각 루트에 바로 등록
    path('agecalc/', include('agecalc.urls')),  # AgeCalc
    path('centurycalc/', include('centurycalc.urls')),  # CenturyCalc
    path('conspiracy/', include('conspiracy.urls')),  # ConspiracyBoard
    path('dischargecalc/', include('dischargecalc.urls')),
    path('worldtime/', include('worldtime.urls')),
    path('visitor-stats/', include('visitorstats.urls')),
    path('bmicalc/', include('bmicalc.urls')),
    path('idgen/', include('idgen.urls')),
    path('pomodoro/', include('pomodoro.urls')),

    path('exchanger/', include('exchanger.urls')),  # 환율 계산기 라우트 추가

    path('scripter/', include('scripter.urls')),

    # 🔥 루트 슬러그 리다이렉트 지원
    path('<slug:slug>/', redirect_short_link),

    re_path(r'^(?P<slug>[a-zA-Z0-9]+)$', redirect_short_link),  # 슬래시 없는 것도 지원


]


handler404 = 'common.views.page_not_found'
handler500 = 'common.views.server_error'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
