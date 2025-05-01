from datetime import date
from .models import Visit

class VisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/tools/visitor-stats/'):
            today = date.today().isoformat()
            if request.session.get('visited_date') != today:
                ip = request.META.get('REMOTE_ADDR')
                user = request.user if request.user.is_authenticated else None
                Visit.objects.create(ip_address=ip, user=user)
                request.session['visited_date'] = today
        return self.get_response(request)
