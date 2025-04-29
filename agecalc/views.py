# agecalc/views.py

from django.shortcuts import render
from datetime import date
import lunardate

def index(request):
    # today: YYYY-MM-DD 형식으로 템플릿에 넘겨줍니다
    return render(request, 'agecalc/index.html', {
        'today': date.today().isoformat()
    })

def calculate(request):
    bd        = request.POST.get('birth_date','').strip()
    td_str    = request.POST.get('target_date','').strip()
    use_lunar = request.POST.get('use_lunar') == 'on'

    # 기준일이 없으면 today
    if not td_str:
        td_str = date.today().isoformat()

    # 생년월일 파싱
    try:
        y1, m1, d1 = map(int, bd.split('-'))
    except:
        return render(request, 'agecalc/index.html', {
            'error': '생년월일을 YYYY-MM-DD 형식으로 입력해주세요.',
            'today': date.today().isoformat()
        })

    # 음력 변환 or 양력
    if use_lunar:
        birth = lunardate.LunarDate(y1, m1, d1).toSolarDate()
    else:
        from datetime import date as _date
        birth = _date(y1, m1, d1)

    # 기준일 파싱
    from datetime import date as _date
    y2, m2, d2 = map(int, td_str.split('-'))
    target = _date(y2, m2, d2)

    # 만나이·한국식 나이 계산
    age        = y2 - birth.year - ((m2, d2) < (birth.month, birth.day))
    korean_age = y2 - birth.year + 1

    return render(request, 'agecalc/result.html', {
        'age': age,
        'korean_age': korean_age,
        'birth_date': birth,
        'target_date': target,
    })
