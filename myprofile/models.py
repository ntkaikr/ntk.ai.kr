from django.db import models
from django.contrib.auth.models import User
from toolhub.models import Tool  # 툴 모델 import

# myprofile/models.py

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(
        max_length=10,
        choices=[('free', '프리'), ('basic', '베이직'), ('premium', '프리미엄')],
        default='free'
    )
    frequent_tools = models.ManyToManyField(Tool, blank=True, related_name='favored_by')

    def tool_limit(self):
        return {
            'free': 3,
            'basic': 10,
            'premium': 30
        }.get(self.plan, 3)

    def __str__(self):
        return f"{self.user.username}님의 프로필"
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    frequent_tools = models.ManyToManyField(Tool, blank=True, related_name='frequent_by')

    def tool_limit(self):
        # 요금제에 따라 최대 등록 수를 제한 (추후 확장 가능)
        plan = getattr(self, 'plan', 'free')  # plan 필드는 선택적으로 도입
        return {
            'free': 3,
            'basic': 10,
            'premium': 30
        }.get(plan, 3)

    def __str__(self):
        return f"{self.user.username}의 프로필"
"""

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_datetime = models.DateTimeField(null=True, blank=True)  # ← 수정된 필드
    done_at = models.DateTimeField(null=True, blank=True)  # ✅ 추가

    def __str__(self):
        return f"[{'✅' if self.is_done else '❌'}] {self.content}"
