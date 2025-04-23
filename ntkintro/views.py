from django.shortcuts import render
from .models import NTKIntro

def intro_page(request):
    # 가장 최근 버전 기준으로 하나 가져오기
    intro = NTKIntro.objects.order_by('-created_at').first()
    return render(request, 'ntkintro/intro_page.html', {'intro': intro})
