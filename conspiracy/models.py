# conspiracy/models.py

from django.db import models
from django.conf import settings

class BoardPost(models.Model):
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title      = models.CharField(max_length=200)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# User 모델에 구독 플래그 추가 (마이그레이션 필요)
from django.contrib.auth import get_user_model
User = get_user_model()
if not hasattr(User, 'is_conspirator'):
    User.add_to_class('is_conspirator', models.BooleanField(default=False))
