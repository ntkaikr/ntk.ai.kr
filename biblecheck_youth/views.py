from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import render, get_object_or_404
from .models import Book, ChapterCheck
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def today_checked(request):
    today = date.today()
    records = ChapterCheck.objects.filter(user=request.user, date_checked=today).select_related('book').order_by('book__testament', 'book__name', 'chapter')

    context = {
        'records': records,
        'today': today,
    }
    return render(request, 'biblecheck_youth/today_checked.html', context)


@login_required
def history_checked(request):
    records = ChapterCheck.objects.filter(user=request.user).select_related('book').order_by('-date_checked', 'book__testament', 'book__name', 'chapter')

    context = {
        'records': records,
    }
    return render(request, 'biblecheck_youth/history_checked.html', context)

@login_required
def check_chapter(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        selected = request.POST.get('selected_chapters', '')
        chapter_list = [int(c.strip()) for c in selected.split(',') if c.strip().isdigit()]

        for chapter in chapter_list:
            ChapterCheck.objects.get_or_create(user=request.user, book=book, chapter=chapter)

    #return redirect('biblecheck_youth:chapter_list', book_id=book_id)
    # ✅ 변경된 리다이렉트: 오늘의 체크 화면으로
    return redirect('biblecheck_youth:today_checked')


def chapter_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    checked_chapters = ChapterCheck.objects.filter(user=request.user, book=book).values_list('chapter', flat=True)
    chapters = range(1, book.total_chapters + 1)

    context = {
        'book': book,
        'chapters': chapters,
        'checked_chapters': checked_chapters,
    }
    return render(request, 'biblecheck_youth/chapter_list.html', context)

def book_list(request):
    selected_testament = request.GET.get('testament')  # 'OT' 또는 'NT'

    ot_books = Book.objects.filter(testament='OT').order_by('id') if selected_testament == 'OT' else []
    nt_books = Book.objects.filter(testament='NT').order_by('id') if selected_testament == 'NT' else []

    context = {
        'selected_testament': selected_testament,
        'ot_books': ot_books,
        'nt_books': nt_books,
    }
    return render(request, 'biblecheck_youth/book_list.html', context)

