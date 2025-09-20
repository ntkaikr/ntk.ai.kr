# apps/nickgen/models.py
from django.conf import settings
from django.db import models


class SavedNickname(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_nicknames')
    text = models.CharField(max_length=64, db_index=True)
    style = models.CharField(max_length=20, blank=True)
    lang = models.CharField(max_length=10, blank=True)
    seed = models.CharField(max_length=32, blank=True)
    tags = models.CharField(max_length=128, blank=True, help_text='쉼표로 구분')
    copied_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'text')


    def __str__(self):
        return self.text