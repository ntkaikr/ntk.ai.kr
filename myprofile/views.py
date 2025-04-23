from .models import Todo
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import redirect
from toolhub.models import Tool
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from toolhub.models import Tool
from .models import Todo, Profile


@login_required
def profile_view(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)

    frequent_tools = profile.frequent_tools.all()
    todos = Todo.objects.filter(user=user).order_by('-created_at')
    all_tools = Tool.objects.all()

    context = {
        'user': user,
        'frequent_tools': frequent_tools,
        'todos': todos,
        'all_tools': all_tools,
    }
    return render(request, 'myprofile/view.html', context)


@login_required
def add_frequent_tool(request):
    if request.method == 'POST':
        tool_id = request.POST.get('tool_id')
        tool = Tool.objects.filter(id=tool_id).first()
        profile, _ = Profile.objects.get_or_create(user=request.user)

        if tool:
            max_allowed = profile.tool_limit()

            if profile.frequent_tools.count() >= max_allowed:
                messages.error(request, f"현재 요금제({profile.plan})에서는 최대 {max_allowed}개까지만 등록할 수 있습니다.")
            elif tool in profile.frequent_tools.all():
                messages.warning(request, "이미 등록된 도구입니다.")
            else:
                profile.frequent_tools.add(tool)
                messages.success(request, f"{tool.name} 도구가 자주 사용하는 도구로 추가되었습니다.")

    return redirect('myprofile:view')




@require_POST
@login_required
def add_todo(request):
    content = request.POST.get('content')
    due_date = request.POST.get('due_date')
    due_time = request.POST.get('due_time')

    due_datetime = None
    if due_date:
        from datetime import datetime
        due_time = due_time or "00:00"
        due_datetime = datetime.strptime(f"{due_date} {due_time}", "%Y-%m-%d %H:%M")

    if content:
        Todo.objects.create(user=request.user, content=content, due_datetime=due_datetime)

    return redirect('myprofile:view')


@login_required
def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.is_done = not todo.is_done
    todo.done_at = timezone.now() if todo.is_done else None  # ✅ 체크 시 시간 기록
    todo.save()
    return redirect('myprofile:view')


@login_required
def delete_todo(request, todo_id):
    Todo.objects.filter(id=todo_id, user=request.user).delete()
    return redirect('myprofile:view')

@login_required
def profile_intro(request):
    return render(request, 'myprofile/intro.html')

