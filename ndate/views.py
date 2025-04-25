from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DDay
from .forms import DDayForm

@login_required
def dday_list(request):
    # ① 로그인한 사용자 본인의 DDay만 조회
    items = DDay.objects.filter(user=request.user).order_by('-created_at')

    form = DDayForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        dday = form.save(commit=False)
        dday.user = request.user
        dday.save()
        return redirect('ndate:dday_list')

    return render(request, 'ndate/dday_list.html', {
        'form': form,
        'items': items,
    })

@login_required
def dday_delete(request, pk):
    obj = get_object_or_404(DDay, pk=pk, user=request.user)
    if request.method == 'POST':
        obj.delete()
        return redirect('ndate:dday_list')
    return render(request, 'ndate/dday_confirm_delete.html', {'obj': obj})
