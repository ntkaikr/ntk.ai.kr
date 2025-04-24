# config/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from accounts.forms import BootstrapAuthenticationForm
from linkn.views import redirect_short_link

urlpatterns = [
    # 1) allauth: 소셜/계정 관리
    #path('accounts/', include('allauth.urls')),

    # 2) 관리자
    path('admin/', admin.site.urls),

    # 3) 커스텀 로그인/로그아웃
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=BootstrapAuthenticationForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # 4) 자체 회원가입 뷰
    path('accounts/', include('accounts.urls')),

    # 5) 내부 도구 모음 (로그인 필요)
    path('tools/', include('toolhub.urls')),

    # 6) 루트 접근 시 자동 리다이렉트
    path('', lambda request: redirect('toolhub:tool_list')),

    # 7) 기타 앱들
    path('biblecheck/', include('biblecheck.urls')),
    path('common/',      include('common.urls')),
    path('ntkintro/',    include('ntkintro.urls')),
    path('youth/',       include('biblecheck_youth.urls')),
    path('linkn/',       include('linkn.urls')),
    path('myprofile/',   include('myprofile.urls')),
    path('carded/',      include('carded.urls')),

    # 8) ShortLink 슬러그 리다이렉트
    path('<slug:slug>/',            redirect_short_link),
    re_path(r'^(?P<slug>[a-zA-Z0-9]+)$', redirect_short_link),
]

handler404 = 'common.views.page_not_found'
handler500 = 'common.views.server_error'

# media 파일 서빙
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
