# centurycalc/views.py

from django.shortcuts import render
from datetime import date

def index(request):
    # 오늘 날짜 넘겨주면 필요 시 기본값으로 활용 가능
    return render(request, 'centurycalc/index.html', {
        'today': date.today().isoformat()
    })

def calculate(request):
    bd = request.POST.get('birth_date','').strip()
    if not bd:
        # 입력 없이 누를 경우 index 로 돌아가며 경고
        return render(request, 'centurycalc/index.html', {
            'error': '생년월일을 선택해주세요.',
            'today': date.today().isoformat()
        })

    year = int(bd.split('-')[0])
    century = (year - 1) // 100 + 1
    span = f"{(century-1)*100+1} ~ {century*100}년"

    return render(request, 'centurycalc/result.html', {
        'century': century,
        'span': span,
    })
