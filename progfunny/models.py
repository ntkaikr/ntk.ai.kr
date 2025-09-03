from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField("제목", max_length=200)
    image = models.ImageField("이미지", upload_to="progfunny/")
    content = models.TextField("내용", blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="progfunny_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="progfunny_comments")
    content = models.TextField("댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.author or '익명'} on {self.post_id}"
