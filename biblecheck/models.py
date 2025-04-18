from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BibleCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    book = models.CharField(max_length=50)      # 예: 창세기, 마태복음
    chapter = models.PositiveIntegerField()     # 몇 장

    def __str__(self):
        return f"{self.user.username} - {self.book} {self.chapter}장 ({self.date})"
