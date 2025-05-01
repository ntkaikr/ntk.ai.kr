# bmicalc/views.py
from django.shortcuts import render

def index(request):
    bmi = None
    category = None
    if request.method == 'POST':
        h = float(request.POST.get('height', 0)) / 100  # cm → m
        w = float(request.POST.get('weight', 0))
        if h > 0:
            bmi = round(w / (h*h), 2)
            if bmi < 18.5:
                category = '저체중'
            elif bmi < 23:
                category = '정상'
            elif bmi < 25:
                category = '과체중'
            else:
                category = '비만'
    return render(request, 'bmicalc/index.html', {
        'bmi': bmi, 'category': category
    })
