# pomodoro/admin.py

from django.contrib import admin
from .models import PomodoroSession

@admin.register(PomodoroSession)
class PomodoroSessionAdmin(admin.ModelAdmin):
    list_display   = ('user', 'date', 'count')
    list_filter    = ('date', 'user')
    search_fields  = ('user__username',)
    ordering       = ('-date', 'user')
    date_hierarchy = 'date'
