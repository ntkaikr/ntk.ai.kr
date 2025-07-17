from django.db import models
from django.contrib.auth.models import User

class Script(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Character(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Scene(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    time_of_day = models.CharField(max_length=50, blank=True)
    mood = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.script.title} - 씬 {self.order}: {self.title}"

class Dialogue(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    line = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.character.name}: {self.line[:30]}"
