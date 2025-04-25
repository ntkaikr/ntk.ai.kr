from django.shortcuts import render
from lorem_text import lorem
from .forms import LoremForm

def generate(request):
    text = ''
    paras = []               # 추가
    if request.method == 'POST':
        form = LoremForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data['paragraphs']
            text = lorem.paragraphs(p)
            paras = text.split('\n\n')   # 뷰에서 분할
    else:
        form = LoremForm()
    return render(request, 'nlorem/generate.html', {
        'form': form,
        'text': text,
        'paras': paras,        # 컨텍스트에 넘겨줌
    })
