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

def future(request):
    context = {}
    if request.method == 'POST':
        bd = request.POST.get('birth_date', '').strip()
        target_year = request.POST.get('target_year', '').strip()

        try:
            y1, m1, d1 = map(int, bd.split('-'))
            birth = date(y1, m1, d1)
            target_year = int(target_year)

            # 기준일: target_year년의 생일 기준
            target_date = date(target_year, birth.month, birth.day)

            # 오늘 날짜로 기준 삼아 (오늘보다 과거인 생일은 1살 적게)
            today = date.today()
            age = target_year - birth.year
            if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
                pass  # 생일 안 지남 → 그냥 target_year - birth_year
            else:
                pass  # 생일 지났음 → 그대로 계산

            context.update({
                'birth_date': birth,
                'target_year': target_year,
                'age_in_target_year': age,
            })

        except:
            context['error'] = '입력값을 확인해주세요.'

    return render(request, 'agecalc/future.html', context)


def goal(request):
    context = {}
    if request.method == 'POST':
        bd = request.POST.get('birth_date', '').strip()
        target_age = request.POST.get('target_age', '').strip()

        try:
            y1, m1, d1 = map(int, bd.split('-'))
            birth = date(y1, m1, d1)
            target_age = int(target_age)

            # 목표 나이가 되는 기본 연도
            goal_year = birth.year + target_age

            context.update({
                'birth_date': birth,
                'target_age': target_age,
                'goal_year': goal_year,
            })

        except:
            context['error'] = '입력값을 확인해주세요.'

    return render(request, 'agecalc/goal.html', context)

def birthday(request):
    context = {}
    if request.method == 'POST':
        bd = request.POST.get('birth_date', '').strip()

        try:
            y1, m1, d1 = map(int, bd.split('-'))
            birth = date(y1, m1, d1)

            today = date.today()
            this_year_birthday = date(today.year, birth.month, birth.day)

            if today >= this_year_birthday:
                status = "지났습니다 🎉"
            else:
                status = "아직 안 지났습니다 🎂"

            context.update({
                'birth_date': birth,
                'status': status,
                'today': today,
            })

        except:
            context['error'] = '입력값을 확인해주세요.'

    return render(request, 'agecalc/birthday.html', context)


def convert(request):
    context = {}
    if request.method == 'POST':
        birth_year = request.POST.get('birth_year', '').strip()
        to_korean = request.POST.get('to_korean') == 'on'  # 체크박스 여부

        try:
            birth_year = int(birth_year)
            today = date.today()

            if to_korean:
                # 만 → 한국식 변환
                result = today.year - birth_year + 1
                mode = "한국 나이"
            else:
                # 한국식 → 만 나이 변환
                result = today.year - birth_year
                mode = "만 나이"

            context.update({
                'birth_year': birth_year,
                'result': result,
                'mode': mode,
                'today_year': today.year,
            })

        except:
            context['error'] = '입력값을 확인해주세요.'

    return render(request, 'agecalc/convert.html', context)


def difference(request):
    context = {}
    if request.method == 'POST':
        bd1 = request.POST.get('birth_date_1', '').strip()
        bd2 = request.POST.get('birth_date_2', '').strip()

        try:
            y1, m1, d1 = map(int, bd1.split('-'))
            y2, m2, d2 = map(int, bd2.split('-'))
            date1 = date(y1, m1, d1)
            date2 = date(y2, m2, d2)

            # 날짜 차이 계산
            delta = abs((date1 - date2).days)
            years = delta // 365
            months = (delta % 365) // 30
            days = (delta % 365) % 30

            # ✨ 추가 계산
            rice_bowls = delta * 3    # 하루 3끼
            rice_cakes = years        # 새해마다 떡국 한 그릇

            context.update({
                'birth_date_1': date1,
                'birth_date_2': date2,
                'years': years,
                'months': months,
                'days': days,
                'total_days': delta,
                'rice_bowls': rice_bowls,
                'rice_cakes': rice_cakes,
            })

        except:
            context['error'] = '입력값을 확인해주세요.'

    return render(request, 'agecalc/difference.html', context)



def sincebirth(request):
    context = {}
    if request.method == 'POST':
        bd = request.POST.get('birth_date', '').strip()

        try:
            y1, m1, d1 = map(int, bd.split('-'))
            birth = date(y1, m1, d1)

            today = date.today()

            # 일수 계산
            delta_days = (today - birth).days
            delta_weeks = delta_days // 7

            # 개월수 계산
            years_diff = today.year - birth.year
            months_diff = today.month - birth.month
            if today.day < birth.day:
                months_diff -= 1
            total_months = years_diff * 12 + months_diff

            context.update({
                'birth_date': birth,
                'today': today,
                'delta_days': delta_days,
                'delta_weeks': delta_weeks,
                'total_months': total_months,
            })

        except:
            context['error'] = '입력값을 확인해주세요.'

    return render(request, 'agecalc/sincebirth.html', context)
