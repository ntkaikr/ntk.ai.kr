# dailyq/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Question(models.Model):
    CATEGORY_CHOICES = [
        ("daily", "일상"),
        ("emotion", "감정"),
        ("social", "관계/사회성"),
        ("imagine", "상상"),
        ("choice", "선택"),
    ]
    text = models.CharField("질문", max_length=255, unique=True)
    category = models.CharField("카테고리", max_length=20, choices=CATEGORY_CHOICES, default="daily")
    difficulty = models.PositiveSmallIntegerField("난이도(1~3)", default=1)
    min_age = models.PositiveSmallIntegerField("권장 최소 나이", default=3)
    max_age = models.PositiveSmallIntegerField("권장 최대 나이", default=7)
    is_active = models.BooleanField("사용 여부", default=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ["category", "difficulty", "id"]

    def __str__(self):
        return f"[{self.get_category_display()}] {self.text}"


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="dailyq_answers")
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="answers")
    date = models.DateField("기록일")  # 오늘 날짜(질문 기준일)
    child_name = models.CharField("아이 이름(선택)", max_length=30, blank=True)
    answer_text = models.TextField("아이의 대답 / 관찰", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "question", "date")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} / {self.question_id} / {self.date}"
