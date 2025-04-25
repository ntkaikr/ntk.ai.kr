from django.contrib import admin
from .models import Category, Tool, Comment, Reply, ToolLike, ToolTag, ToolRunLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'access_level', 'visibility')
    filter_horizontal = ('creators', 'managers', 'allowed_users')  # 🔥 매니저 편집용
    list_filter = ('category', 'access_level', 'visibility')
    search_fields = ('name', 'description')

admin.site.register(ToolRunLog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(ToolLike)
admin.site.register(ToolTag)
