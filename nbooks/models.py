from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    goal_word_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)  # << 추가!

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} - {self.title}"

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.chapter.title} - {self.title}"
