# nlorem/views.py
from django.shortcuts import render
from lorem_text import lorem
from .forms import LoremForm

def generate(request):
    paras = []
    if request.method == 'POST':
        form = LoremForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data['paragraphs']
            # lorem.paragraph() 을 p번 호출해 명확히 문단 리스트 생성
            paras = [lorem.paragraph() for _ in range(p)]
    else:
        form = LoremForm()
    return render(request, 'nlorem/generate.html', {
        'form': form,
        'paras': paras,
    })
