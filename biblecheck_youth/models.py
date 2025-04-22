from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    TESTAMENT_CHOICES = [
        ('OT', '구약'),
        ('NT', '신약'),
    ]
    name = models.CharField(max_length=50)
    testament = models.CharField(max_length=2, choices=TESTAMENT_CHOICES)
    total_chapters = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ChapterCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.PositiveIntegerField()
    date_checked = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book', 'chapter')

    def __str__(self):
        return f'{self.user.username} - {self.book.name} {self.chapter}장'
