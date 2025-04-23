from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='carded/profile/', blank=True, null=True)
    show_public = models.BooleanField(default=True)

    PLAN_CHOICES = [
        ('free', '프리'),
        ('basic', '베이직'),
        ('premium', '프리미엄'),
    ]
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default='free')

    def sns_limit(self):
        return {
            'free': 3,
            'basic': 10,
            'premium': 20,
        }.get(self.plan, 3)

    def __str__(self):
        return f"{self.user.username}님의 명함 (카디드)"


class SocialLink(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='social_links')
    label = models.CharField(max_length=50)
    url = models.URLField()
    favicon_url = models.URLField(blank=True)

    def clean(self):
        # ✅ 카드가 지정되어 있을 때만 제한 검사
        if self.card_id is not None:
            existing_count = self.card.social_links.exclude(id=self.id).count()
            if existing_count >= self.card.sns_limit():
                raise ValidationError(
                    f"{self.card.get_plan_display()} 요금제는 최대 {self.card.sns_limit()}개의 링크만 등록할 수 있습니다."
                )

    def __str__(self):
        return f"{self.card.user.username} - {self.label}"
