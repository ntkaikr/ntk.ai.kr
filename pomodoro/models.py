# pomodoro/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PomodoroSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user} - {self.date} : {self.count}"
