# idgen/views.py
import string, random
from django.shortcuts import render

def index(request):
    generated = None
    length = int(request.GET.get('length', 8))
    if request.method == 'POST':
        try:
            length = int(request.POST.get('length', 8))
        except ValueError:
            length = 8
        chars = string.ascii_letters + string.digits
        generated = ''.join(random.choice(chars) for _ in range(length))
    return render(request, 'idgen/index.html', {
        'generated': generated, 'length': length
    })
