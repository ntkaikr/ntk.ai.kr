# conspiracy/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BoardPost

def post_list(request):
    posts = BoardPost.objects.order_by('-created_at')
    return render(request, 'conspiracy/list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BoardPost, pk=pk)
    return render(request, 'conspiracy/detail.html', {'post': post})

@login_required
def post_create(request):
    # 유료 구독자만
    if not request.user.is_conspirator:
        return redirect('payment:subscribe')  # 결제 페이지 URL 이름
    if request.method == 'POST':
        BoardPost.objects.create(
            author  = request.user,
            title   = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('conspiracy:list')
    return render(request, 'conspiracy/form.html')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(BoardPost, pk=pk, author=request.user)
    if request.method == 'POST':
        post.title   = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('conspiracy:detail', pk=pk)
    return render(request, 'conspiracy/form.html', {'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(BoardPost, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('conspiracy:list')
    return render(request, 'conspiracy/confirm_delete.html', {'post': post})
