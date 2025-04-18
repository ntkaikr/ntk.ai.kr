from django.contrib import admin
from .models import Tool, Comment, Reply, ToolLike, ToolTag, ToolRunLog

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'access_level', 'visibility')
    filter_horizontal = ('allowed_users', 'managers')  # 🔥 매니저 편집용

admin.site.register(ToolRunLog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(ToolLike)
admin.site.register(ToolTag)
