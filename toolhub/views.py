from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from .models import Tool
from .forms import ToolForm
from django.db.models import Avg
from .forms import CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Comment
from .models import ToolLike
from django.http import HttpResponseForbidden
from .models import Tool, ToolRunLog
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def run_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)

    # 권한 체크
    if tool.access_level == 'superuser' and not request.user.is_superuser:
        return HttpResponseForbidden("슈퍼유저만 접근 가능합니다.")
    elif tool.access_level == 'staff' and not request.user.is_staff:
        return HttpResponseForbidden("스태프만 접근 가능합니다.")
    elif tool.access_level == 'level':
        if not hasattr(request.user, 'profile') or tool.allowed_level is None:
            return HttpResponseForbidden("접근 권한이 없습니다.")
        elif request.user.profile.level < tool.allowed_level:
            return HttpResponseForbidden("레벨이 부족합니다.")
    elif tool.access_level == 'user' and request.user not in tool.allowed_users.all():
        return HttpResponseForbidden("지정된 사용자만 접근 가능합니다.")

    # 로그 기록
    ToolRunLog.objects.create(tool=tool, user=request.user)

    # 리디렉션
    return redirect(tool.link)

@login_required
def toggle_tool_like(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    like, created = ToolLike.objects.get_or_create(tool=tool, user=request.user)

    if not created:
        like.delete()  # 좋아요 취소
    return redirect('toolhub:tool_detail', pk=tool.pk)

@login_required
def toggle_comment_like(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.is_liked_by(request.user):
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('toolhub:tool_detail', args=[comment.tool.id]))

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    comment_form = CommentForm()
    reply_form = ReplyForm()
    admin_user = User.objects.get(username='admin')

    # 평균 별점 계산
    average_rating = tool.comments.aggregate(avg=Avg('stars'))['avg'] or 0
    rounded = round(average_rating)

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.tool = tool
                comment.author = request.user
                comment.save()
                return redirect('toolhub:tool_detail', pk=pk)

        elif 'reply_submit' in request.POST:
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.author = request.user
                reply.parent_comment_id = request.POST.get('parent_id')
                reply.save()
                return redirect('toolhub:tool_detail', pk=pk)

    return render(request, 'toolhub/tool_detail.html', {
        'tool': tool,
        'comment_form': comment_form,
        'reply_form': reply_form,
        'average_rating': average_rating,
        'average_rating_rounded': rounded,
        'admin_user': admin_user,
    })


@user_passes_test(lambda u: u.is_superuser)
def tool_create(request):
    if request.method == 'POST':
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save()
            return redirect('toolhub:tool_detail', pk=tool.pk)
    else:
        form = ToolForm()
    return render(request, 'toolhub/tool_form.html', {'form': form})

def tool_list(request):
    q = request.GET.get('q', '')
    tools = Tool.objects.all()
    if q:
        tools = tools.filter(name__icontains=q)
    return render(request, 'toolhub/tool_list.html', {'tools': tools})
