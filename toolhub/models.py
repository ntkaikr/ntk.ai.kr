from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone  # 꼭 추가

User = get_user_model()

class Tool(models.Model):
    VISIBILITY_CHOICES = [
        ('public', '공개'),
        ('private', '비공개'),
    ]

    ACCESS_LEVEL_CHOICES = [
        ('all', '비회원 포함 전체'),
        ('members', '로그인한 회원'),
        ('level', '특정 레벨 이상'),
        ('user', '지정 사용자'),
        ('staff', '관리자'),
        ('superuser', '슈퍼유저'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES, default='members')
    allowed_level = models.PositiveIntegerField(null=True, blank=True)
    allowed_users = models.ManyToManyField(User, blank=True, related_name='permitted_tools')

    thumbnail = models.ImageField(upload_to='tool_thumbnails/', blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text="툴 실행용 링크 주소")

    managers = models.ManyToManyField(User, blank=True, related_name='managed_tools', help_text="이 툴의 관리자")

    def average_rating(self):
        comments = self.comments.all()
        if comments.exists():
            return round(comments.aggregate(models.Avg('stars'))['stars__avg'], 1)
        return 0.0

    def total_likes(self):
        return self.likes.count()

    def total_likes(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(user=user).exists()

    def __str__(self):
        return self.name

class ToolRunLog(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 한국 시간으로 변환
        local_time = timezone.localtime(self.accessed_at)
        formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
        return f"{self.user.username} ran {self.tool.name} at {formatted_time}"


class Comment(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    stars = models.PositiveSmallIntegerField(default=5)  # 1~5점
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def like_count(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

    def __str__(self):
        return f"{self.author} on {self.tool}"

class Reply(models.Model):
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.author} on {self.parent_comment.id}"

class ToolLike(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('tool', 'user')  # 중복 좋아요 방지

    def __str__(self):
        return f"{self.user} likes {self.tool}"

class ToolTag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    tools = models.ManyToManyField(Tool, related_name='tags')

    def __str__(self):
        return self.name
