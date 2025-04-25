from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from .forms import ToolForm
from django.db.models import Avg
from .forms import CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Comment
from .models import ToolLike
from django.http import HttpResponseForbidden
from .models import Tool, ToolRunLog, Category
from django.contrib.auth import get_user_model
from myprofile.models import Profile
from django.contrib import messages
from django.db.models import Q


User = get_user_model()

@login_required
def pin_tool_to_profile(request, tool_id):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    try:
        tool = Tool.objects.get(id=tool_id)
    except Tool.DoesNotExist:
        messages.error(request, "해당 도구를 찾을 수 없습니다.")
        return redirect('toolhub:tool_list')  # fallback

    if profile.frequent_tools.filter(id=tool_id).exists():
        messages.warning(request, "이미 등록된 도구입니다.")
    elif profile.frequent_tools.count() >= profile.tool_limit():
        messages.error(request, f"요금제({profile.plan})에서는 최대 {profile.tool_limit()}개까지만 등록할 수 있습니다.")
    else:
        profile.frequent_tools.add(tool)
        messages.success(request, f"{tool.name} 도구가 자주 사용하는 도구에 추가되었습니다.")

    return redirect('toolhub:tool_detail', tool_id=tool_id)

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

    # 🔹 툴 실행 로그
    ToolRunLog.objects.create(tool=tool, user=request.user)

    # 🔸 특수 처리: 이름이 '카디드'인 경우 명함으로 이동
    if tool.name.lower() in ['카디드', 'carded']:
        return redirect('carded:public_card_by_username', username=request.user.username)

    # 🔹 일반적인 링크 실행
    if tool.link:
        return redirect(tool.link)

    # 🔸 링크 없음 → 툴 상세로 fallback
    return redirect('toolhub:tool_detail', pk=tool.pk)

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

def tool_list(request):
    q = request.GET.get('q', '').strip()
    cat_slug = request.GET.get('category', '').strip()

    # 모든 카테고리(탭) 가져오기
    categories = Category.objects.all()

    # 내 즐겨찾기 ID 목록
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        fav_ids = list(profile.frequent_tools.values_list('id', flat=True))
    else:
        fav_ids = []

    # 1) 기본 쿼리셋
    base_qs = Tool.objects.all()

    # 2) 카테고리 필터
    if cat_slug == 'favorites':
        # 즐겨찾기 탭
        base_qs = base_qs.filter(id__in=fav_ids)
    elif cat_slug:
        # 일반 카테고리 탭
        base_qs = base_qs.filter(category__slug=cat_slug)

    # 3) 검색 필터 (항상 적용)
    if q:
        base_qs = base_qs.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q)
        )

    # 4) 즐겨찾기한 도구와 나머지 분리
    favorite_qs = base_qs.filter(id__in=fav_ids)
    other_qs    = base_qs.exclude(id__in=fav_ids).order_by('-created_at')

    tools = list(favorite_qs) + list(other_qs)

    return render(request, 'toolhub/tool_list.html', {
        'tools': tools,
        'frequent_tools': favorite_qs,
        'categories': categories,
        'current_category': cat_slug,
        'search_query': q,
    })
