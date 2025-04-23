from django.contrib import admin
from .models import Card, SocialLink

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'show_public')
    inlines = [SocialLinkInline]

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('card', 'label', 'url')
