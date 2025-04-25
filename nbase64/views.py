import base64
from django.shortcuts import render
from .forms import Base64Form

def base64_tool(request):
    result = None
    error = None
    if request.method == 'POST':
        form = Base64Form(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            action = form.cleaned_data['action']
            try:
                if action == 'encode':
                    result = base64.b64encode(text.encode()).decode()
                else:
                    result = base64.b64decode(text).decode()
            except Exception as e:
                error = f"처리 오류: {e}"
    else:
        form = Base64Form()
    return render(request, 'nbase64/tool.html', {
        'form': form, 'result': result, 'error': error
    })
