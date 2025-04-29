# agecalc/views.py
from django.shortcuts import render
from datetime import date
import lunardate  # pip install lunardate

def index(request):
    return render(request, 'agecalc/index.html')

def calculate(request):
    bd        = request.POST['birth_date']
    td_str    = request.POST.get('target_date', date.today().isoformat())
    use_lunar = request.POST.get('use_lunar') == 'on'

    y1, m1, d1 = map(int, bd.split('-'))
    if use_lunar:
        birth = lunardate.LunarDate(y1, m1, d1).toSolarDate()
    else:
        birth = date(y1, m1, d1)

    y2, m2, d2 = map(int, td_str.split('-'))
    target = date(y2, m2, d2)

    age        = y2 - birth.year - ((m2, d2) < (birth.month, birth.day))
    korean_age = y2 - birth.year + 1

    return render(request, 'agecalc/result.html', {
        'age': age,
        'korean_age': korean_age,
        'birth_date': birth,
        'target_date': target,
    })
