from django.db import models
import uuid
import random
import string


class ShortLink(models.Model):
    original_url = models.URLField()
    slug = models.SlugField(unique=True, max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.slug} → {self.original_url}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self, length=6):
        while True:
            slug = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            if not ShortLink.objects.filter(slug=slug).exists():
                return slug
