import csv
from django.core.management.base import BaseCommand
from biblecheck_youth.models import Book

class Command(BaseCommand):
    help = 'CSV 파일로부터 Book 데이터 등록'

    def handle(self, *args, **kwargs):
        with open('bible_books_youth.csv', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Book.objects.get_or_create(
                    name=row['name'],
                    testament=row['testament'],
                    total_chapters=int(row['total_chapters'])
                )
        self.stdout.write(self.style.SUCCESS('✅ Book 데이터 등록 완료!'))
