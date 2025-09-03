from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Residence(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="unit_residences")
    floor = models.PositiveIntegerField("층")
    room_number = models.CharField("호수", max_length=10)   # 예: 101호
    resident = models.CharField("거주자", max_length=50, blank=True, null=True)
    note = models.CharField("비고", max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-floor", "room_number"]

    def __str__(self):
        return f"{self.floor}층 {self.room_number}"
