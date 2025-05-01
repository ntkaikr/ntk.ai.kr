from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Visit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    visited_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user or '익명'} @ {self.visited_at.date()}"
