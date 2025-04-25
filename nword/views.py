from django.shortcuts import render
from .forms import CountForm

def count(request):
    char_count = word_count = None
    if request.method == 'POST':
        form = CountForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data['content']
            char_count = len(c)
            word_count = len([w for w in c.split() if w])
    else:
        form = CountForm()
    return render(request, 'nword/count.html', {
        'form': form,
        'char_count': char_count,
        'word_count': word_count,
    })
