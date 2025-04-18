from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class NTKIntro(models.Model):
    title = models.CharField(max_length=100, default="NTK Internal Tools")
    logo = models.ImageField(upload_to='ntk_intro/', blank=True, null=True)
    description = models.TextField()
    current_version = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VersionHistory(models.Model):
    intro = models.ForeignKey(NTKIntro, on_delete=models.CASCADE, related_name='version_history')
    version = models.CharField(max_length=50)
    changes = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.version} - {self.updated_at.date()}"
