# dailyq/views.py
import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import AnswerForm
from .models import Answer, Question
from .services import get_today_question


@login_required
def index(request):
    """오늘의 질문 + 답변 기록"""
    today = timezone.localdate()
    category = request.GET.get("category")  # ?category=daily 등
    q = get_today_question(today, category=category)
    if q is None:
        raise Http404("활성화된 질문이 없습니다. 관리자에서 질문을 추가하세요.")

    # 기존 기록이 있으면 폼 초기값으로
    existing = Answer.objects.filter(user=request.user, question=q, date=today).first()
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=existing)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.user = request.user
            ans.question = q
            ans.date = today
            ans.save()
            return redirect("dailyq_index")
    else:
        if existing:
            form = AnswerForm(instance=existing)
        else:
            form = AnswerForm()

    context = {
        "question": q,
        "form": form,
        "today": today,
        "category": category or "",
        "has_existing": bool(existing),
    }
    return render(request, "dailyq/index.html", context)


@login_required
def history(request):
    """내 답변 히스토리 + 간단 통계"""
    qs = Answer.objects.filter(user=request.user).select_related("question")
    category = request.GET.get("category")
    if category:
        qs = qs.filter(question__category=category)

    paginator = Paginator(qs, 10)
    page = paginator.get_page(request.GET.get("page"))

    # 간단 통계
    total = qs.count()
    by_cat = (
        qs.values("question__category")
          .order_by("question__category")
          .distinct()
    )
    # 연속 기록(스reak) 계산: 최근부터 날짜 쭉 이어지는 길이
    streak = _calc_streak(Answer.objects.filter(user=request.user))

    context = {
        "page": page,
        "total": total,
        "category": category or "",
        "streak": streak,
    }
    return render(request, "dailyq/history.html", context)


def _calc_streak(qs_all):
    """오늘부터 역방향으로 연속 기록 일수"""
    dates = list(qs_all.values_list("date", flat=True).order_by("-date"))
    if not dates:
        return 0
    today = timezone.localdate()
    curr = today
    streak = 0
    seen = set(dates)
    while curr in seen:
        streak += 1
        curr = curr - datetime.timedelta(days=1)
    return streak


@login_required
def api_today(request):
    """JSON: 오늘의 질문 보기 (간단 연동용)"""
    today = timezone.localdate()
    category = request.GET.get("category")
    q = get_today_question(today, category=category)
    if not q:
        return JsonResponse({"error": "no_active_question"}, status=404)
    return JsonResponse({
        "date": today.isoformat(),
        "question": q.text,
        "category": q.category,
        "difficulty": q.difficulty,
        "age": {"min": q.min_age, "max": q.max_age},
    })
