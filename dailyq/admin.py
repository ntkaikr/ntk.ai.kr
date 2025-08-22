# dailyq/admin.py
from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "category", "difficulty", "min_age", "max_age", "is_active", "created_at")
    list_filter = ("category", "difficulty", "is_active")
    search_fields = ("text",)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "question", "date", "child_name", "created_at")
    list_filter = ("date", "question__category")
    search_fields = ("child_name", "answer_text")
