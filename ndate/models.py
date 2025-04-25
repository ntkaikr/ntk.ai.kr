from django.db import models
from django.conf import settings
from django.utils import timezone

class DDay(models.Model):
    user        = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ddays'
    )
    target_date = models.DateField()
    title       = models.CharField("제목/내용", max_length=100, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def days_diff(self):
        diff = (self.target_date - timezone.localdate()).days
        return diff

    def status_label(self):
        d = self.days_diff()
        if d > 0:    return f"D-{d}"
        if d < 0:    return f"+{abs(d)}"
        return "D-Day!"

    def __str__(self):
        return f"{self.title or self.target_date} ({self.status_label()})"
