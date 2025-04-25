from django.db import models
from django.utils import timezone


class DDay(models.Model):
    target_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def days_diff(self):
        diff = (self.target_date - timezone.localdate()).days
        return diff

    def status_label(self):
        d = self.days_diff()
        if d > 0:    return f"D-{d}"
        if d < 0:    return f"+{abs(d)}"
        return "D-Day!"

    def __str__(self):
        return f"{self.target_date} ({self.status_label()})"
