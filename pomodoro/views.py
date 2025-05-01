# pomodoro/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import PomodoroSession


@login_required
def timer(request):
    today = timezone.localdate()
    session, _ = PomodoroSession.objects.get_or_create(user=request.user, date=today)
    # 최근 5일 세션 기록
    sessions = (PomodoroSession.objects
                .filter(user=request.user)
                .order_by('-date')[:5])
    return render(request, 'pomodoro/timer.html', {
        'count': session.count,
        'sessions': sessions,
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
