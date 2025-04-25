from django.shortcuts import render
from .forms import UnitForm

def unit_tool(request):
    result = None
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            v = form.cleaned_data['value']
            c = form.cleaned_data['conversion']
            if c == 'km_m': result = v * 1000
            elif c == 'm_km': result = v / 1000
            elif c == 'kg_g': result = v * 1000
            elif c == 'g_kg': result = v / 1000
            elif c == 'c_f': result = v * 9/5 + 32
            elif c == 'f_c': result = (v - 32) * 5/9
    else:
        form = UnitForm()
    return render(request, 'nunit/tool.html', {'form': form, 'result': result})
