# myprofile/admin.py
from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'is_done', 'due_date', 'created_at')
    list_filter = ('is_done', 'due_date')
    search_fields = ('content',)
