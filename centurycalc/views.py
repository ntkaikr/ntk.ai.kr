# centurycalc/views.py

from django.shortcuts import render
from datetime import date

def index(request):
    # 계산 폼 페이지
    return render(request, 'centurycalc/index.html')

def calculate(request):
    # 폼 데이터 파싱
    bd = request.POST['birth_date']            # ex. '1990-05-23'
    year = int(bd.split('-')[0])
    # 세기 계산: 1~100년 → 1세기, 101~200년 → 2세기 …
    century = (year - 1) // 100 + 1
    span = f"{(century-1)*100+1} ~ {century*100}년"

    return render(request, 'centurycalc/result.html', {
        'century': century,
        'span': span,
    })
