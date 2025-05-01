from django.shortcuts import render
from datetime import date
from .models import Visit

def dashboard(request):
    today = date.today()
    today_count = Visit.objects.filter(visited_at__date=today).count()
    total_count = Visit.objects.count()

    return render(request, 'visitorstats/dashboard.html', {
        'today_count': today_count,
        'total_count': total_count,
    })
