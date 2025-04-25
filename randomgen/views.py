import random
from django.shortcuts import render
from .forms import RandomForm

def random_generator(request):
    result = []
    if request.method == 'POST':
        form = RandomForm(request.POST)
        if form.is_valid():
            lo = form.cleaned_data['min_value']
            hi = form.cleaned_data['max_value']
            n  = form.cleaned_data['count']
            result = [random.randint(lo, hi) for _ in range(n)]
    else:
        form = RandomForm()

    return render(request, 'randomgen/random_generator.html', {
        'form': form,
        'result': result,
    })
