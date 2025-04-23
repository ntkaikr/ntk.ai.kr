from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_datetime = models.DateTimeField(null=True, blank=True)  # ← 수정된 필드
    done_at = models.DateTimeField(null=True, blank=True)  # ✅ 추가

    def __str__(self):
        return f"[{'✅' if self.is_done else '❌'}] {self.content}"
