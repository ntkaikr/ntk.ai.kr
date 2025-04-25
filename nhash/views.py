import hashlib
from django.shortcuts import render
from .forms import HashForm

def hash_tool(request):
    result = None
    if request.method == 'POST':
        form = HashForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['text'].encode()
            algo = form.cleaned_data['algorithm']
            h = getattr(hashlib, algo)()
            h.update(data)
            result = h.hexdigest()
    else:
        form = HashForm()
    return render(request, 'nhash/tool.html', {'form': form, 'result': result})
