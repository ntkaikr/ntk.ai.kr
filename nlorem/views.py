from django.shortcuts import render
from lorem_text import lorem
from .forms import LoremForm

def generate(request):
    text = ''
    if request.method == 'POST':
        form = LoremForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data['paragraphs']
            text = lorem.paragraphs(p)
    else:
        form = LoremForm()
    return render(request, 'nlorem/generate.html', {'form': form, 'text': text})
