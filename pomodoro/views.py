# pomodoro/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import PomodoroSession

@login_required
def timer(request):
    # 오늘 세션 카운트
    today = timezone.localdate()
    session, created = PomodoroSession.objects.get_or_create(
        user=request.user, date=today
    )
    return render(request, 'pomodoro/timer.html', {
        'count': session.count
    })

@login_required
def record(request):
    if request.method == 'POST':
        today = timezone.localdate()
        session, _ = PomodoroSession.objects.get_or_create(
            user=request.user, date=today
        )
        session.count += 1
        session.save()
    return redirect('pomodoro:timer')
