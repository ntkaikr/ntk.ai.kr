from decimal import Decimal
from django.shortcuts import render
from .forms import AveragingForm

def averaging_calculator(request):
    avg_price = None
    total_qty = None

    if request.method == 'POST':
        form = AveragingForm(request.POST)
        if form.is_valid():
            oq, op = form.cleaned_data['old_qty'], form.cleaned_data['old_price']
            nq, np = form.cleaned_data['new_qty'], form.cleaned_data['new_price']
            total_qty = oq + nq
            if total_qty > 0:
                avg_price = (oq * op + nq * np) / total_qty
    else:
        form = AveragingForm()

    return render(request, 'averager/averaging_calculator.html', {
        'form': form,
        'avg_price': avg_price,
        'total_qty': total_qty,
    })
