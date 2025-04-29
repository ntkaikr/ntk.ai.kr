# conspiracy/models.py

from django.db import models
from django.conf import settings

class BoardPost(models.Model):
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title      = models.CharField(max_length=200)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# ─────────── 댓글(Comment) 모델 ───────────
class Comment(models.Model):
    post       = models.ForeignKey(BoardPost, related_name='comments', on_delete=models.CASCADE)
    parent     = models.ForeignKey('self', null=True, blank=True,
                                   related_name='replies', on_delete=models.CASCADE)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='conspiracy_comments', on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

# 기존 User 모델 플래그(유지)
from django.contrib.auth import get_user_model
User = get_user_model()
if not hasattr(User, 'is_conspirator'):
    User.add_to_class('is_conspirator', models.BooleanField(default=False))
