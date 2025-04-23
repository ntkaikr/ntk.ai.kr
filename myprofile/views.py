from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from toolhub.models import Tool  # 자주 쓴 도구용
from .models import Todo
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def profile_view(request):
    user = request.user
    frequent_tools = Tool.objects.all()[:3]  # 임시 처리
    todos = Todo.objects.filter(user=user).order_by('-created_at')

    context = {
        'user': user,
        'frequent_tools': frequent_tools,
        'todos': todos,
    }
    return render(request, 'myprofile/view.html', context)


@require_POST
@login_required
def add_todo(request):
    content = request.POST.get('content')
    due_date = request.POST.get('due_date') or None

    if content:
        Todo.objects.create(user=request.user, content=content, due_date=due_date)

    return redirect('myprofile:view')


@login_required
def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('myprofile:view')


@login_required
def delete_todo(request, todo_id):
    Todo.objects.filter(id=todo_id, user=request.user).delete()
    return redirect('myprofile:view')

@login_required
def profile_intro(request):
    return render(request, 'myprofile/intro.html')

