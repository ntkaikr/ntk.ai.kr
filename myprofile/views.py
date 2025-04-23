from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from toolhub.models import Tool  # 자주 쓴 도구용

@login_required
def profile_intro(request):
    return render(request, 'myprofile/intro.html')

@login_required
def profile_view(request):
    user = request.user

    # 예: 최근 사용 도구 또는 즐겨찾기된 도구 3개 (향후 DB로 전환 가능)
    frequently_used_tools = Tool.objects.all()[:3]  # 임시: 전체에서 3개

    context = {
        'user': user,
        'frequent_tools': frequently_used_tools,
    }
    return render(request, 'myprofile/view.html', context)
