from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post
from .forms import PostForm, CommentForm

def post_list(request):
    qs = Post.objects.all()
    paginator = Paginator(qs, 12)
    page = request.GET.get("page", 1)
    posts = paginator.get_page(page)
    return render(request, "progfunny/post_list.html", {"posts": posts})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "짤이 등록됐어요! 😄")
            return redirect("progfunny:post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "progfunny/post_form.html", {"form": form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cform = CommentForm()
    return render(request, "progfunny/post_detail.html", {"post": post, "cform": cform})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "댓글이 등록됐어요! 💬")
    return redirect("progfunny:post_detail", pk=post.pk)
