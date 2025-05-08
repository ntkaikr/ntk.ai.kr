from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import NTKIntro
from toolhub.models import ToolHistory

@user_passes_test(lambda u: u.is_superuser)
def intro_page(request):
    # 최신 NTKIntro
    intro = NTKIntro.objects.order_by('-created_at').first()

    # 공개된 툴 등록 히스토리 전체(최신순)
    tool_histories = (
        ToolHistory.objects
        .select_related('tool', 'tool__category', 'user')
        .filter(tool__visibility='public')
        .order_by('-created_at')
    )

    return render(request, 'ntkintro/intro_page.html', {
        'intro': intro,
        'tool_histories': tool_histories,
    })
