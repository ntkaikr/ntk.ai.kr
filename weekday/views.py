# weekday/views.py
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from .forms import WeekdayForm

KOR_WEEKDAYS = ["월", "화", "수", "목", "금", "토", "일"]  # Python: Monday=0

def index(request):
    result = None
    form = WeekdayForm(request.GET or None)

    if form.is_valid():
        d = form.cleaned_data["date"]
        result = f"{KOR_WEEKDAYS[d.weekday()]}요일"
    else:
        # 첫 진입 시 오늘 날짜 기본 셋팅
        if not request.GET:
            form = WeekdayForm(initial={"date": datetime.date.today()})

    ctx = {
        "form": form,
        "result": result,
        "today": datetime.date.today().isoformat(),
    }
    return render(request, "weekday/index.html", ctx)

def api(request):
    """?date=YYYY-MM-DD 로 요일 반환 (간단 연동용)"""
    date_str = request.GET.get("date")
    if not date_str:
        return JsonResponse({"error": "date=YYYY-MM-DD 쿼리 필요"}, status=400)
    try:
        y, m, d = map(int, date_str.split("-"))
        dt = datetime.date(y, m, d)
    except Exception:
        return JsonResponse({"error": "날짜 형식이 올바르지 않습니다 (YYYY-MM-DD)."}, status=400)

    return JsonResponse({
        "date": dt.isoformat(),
        "weekday_index": dt.weekday(),          # Monday=0
        "weekday_en": dt.strftime("%A"),
        "weekday_ko": f"{KOR_WEEKDAYS[dt.weekday()]}요일",
    })
