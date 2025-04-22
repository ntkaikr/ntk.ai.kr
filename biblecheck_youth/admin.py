from django.contrib import admin
from .models import Book, ChapterCheck

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'testament', 'total_chapters')
    list_filter = ('testament',)
    search_fields = ('name',)

@admin.register(ChapterCheck)
class ChapterCheckAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'chapter', 'date_checked')
    list_filter = ('book', 'date_checked')
    search_fields = ('user__username', 'book__name')
