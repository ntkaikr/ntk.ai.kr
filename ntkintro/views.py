from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import NTKIntro
from toolhub.models import Tool

#@user_passes_test(lambda u: u.is_superuser)
def intro_page(request):
    # 최신 NTKIntro
    intro = NTKIntro.objects.order_by('-created_at').first()

    # 공개된 툴 전체를 최신순으로 가져오기
    tools = (
        Tool.objects
        .select_related('category')
        .filter(visibility='public')
        .order_by('-created_at')
    )

    return render(request, 'ntkintro/intro_page.html', {
        'intro': intro,
        'tools': tools,
    })
