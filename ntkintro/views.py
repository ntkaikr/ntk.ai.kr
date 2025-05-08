from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import NTKIntro
from toolhub.forms import ToolForm
from toolhub.models import ToolHistory

@user_passes_test(lambda u: u.is_superuser)
def intro_page(request):
    # 최신 NTKIntro
    intro = NTKIntro.objects.order_by('-created_at').first()

    # 최근 공개 툴 등록 히스토리 10개
    tool_histories = (
        ToolHistory.objects
        .select_related('tool', 'user')
        .filter(tool__visibility='public')
        .order_by('-created_at')[:10]
    )

    # 신규 툴 등록 처리
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.save()
            tool.creators.add(request.user)
            ToolHistory.objects.create(
                tool=tool,
                user=request.user,
                action='등록'
            )
            return redirect('ntkintro:intro_page')
    else:
        form = ToolForm()

    return render(request, 'ntkintro/intro_page.html', {
        'intro': intro,
        'form': form,
        'tool_histories': tool_histories,
    })
