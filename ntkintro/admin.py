from django.contrib import admin
from .models import NTKIntro, VersionHistory

class VersionInline(admin.TabularInline):
    model = VersionHistory
    extra = 1

@admin.register(NTKIntro)
class NTKIntroAdmin(admin.ModelAdmin):
    inlines = [VersionInline]
