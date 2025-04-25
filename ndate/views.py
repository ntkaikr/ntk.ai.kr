from django.shortcuts import render, redirect, get_object_or_404
from .models import DDay
from .forms import DDayForm

def dday_list(request):
    # 저장된 모든 DDay
    items = DDay.objects.order_by('-created_at')
    form  = DDayForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ndate:dday_list')
    return render(request, 'ndate/dday_list.html', {
        'form': form, 'items': items
    })

def dday_delete(request, pk):
    obj = get_object_or_404(DDay, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('ndate:dday_list')
    return render(request, 'ndate/dday_confirm_delete.html', {'obj': obj})
