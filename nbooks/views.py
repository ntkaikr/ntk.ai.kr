from django.shortcuts import render, redirect
from .forms import BookForm, ChapterForm, SectionForm
from .models import Book, Chapter, Section
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def delete_section(request, section_id):
    section = get_object_or_404(Section, id=section_id, chapter__book__owner=request.user)
    book_id = section.chapter.book.id

    if request.method == 'POST':
        section.delete()
        return redirect('book_detail', book_id=book_id)

    return render(request, 'nbooks/delete_section_confirm.html', {'section': section})

@login_required
def edit_section(request, section_id):
    section = get_object_or_404(Section, id=section_id, chapter__book__owner=request.user)

    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=section.chapter.book.id)
    else:
        form = SectionForm(instance=section)

    return render(request, 'nbooks/edit_section.html', {'form': form, 'section': section})

@login_required
def edit_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id, book__owner=request.user)

    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=chapter.book.id)
    else:
        form = ChapterForm(instance=chapter)

    return render(request, 'nbooks/edit_chapter.html', {'form': form, 'chapter': chapter})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'nbooks/edit_book.html', {'form': form, 'book': book})


@login_required
def read_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # 본인 책이 아니고 비공개면 404
    if not book.is_public and book.owner != request.user:
        return render(request, '404.html', status=404)

    chapters = book.chapters.all().order_by('order')

    return render(request, 'nbooks/read_book.html', {'book': book, 'chapters': chapters})

@login_required
def book_list(request):
    books = Book.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'nbooks/book_list.html', {
        'books': books,
        'view_mode': 'my',  # <= view_mode 누락 방지
    })

@login_required
def public_book_list(request):
    books = Book.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'nbooks/book_list.html', {'books': books, 'view_mode': 'public'})

@login_required
def create_section(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id, book__owner=request.user)
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.chapter = chapter
            section.save()
            return redirect('book_detail', book_id=chapter.book.id)
    else:
        form = SectionForm()
    return render(request, 'nbooks/create_section.html', {'form': form, 'chapter': chapter})


@login_required
def create_chapter(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.book = book
            chapter.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = ChapterForm()
    return render(request, 'nbooks/create_chapter.html', {'form': form, 'book': book})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)
    chapters = book.chapters.all().order_by('order')

    total_word_count = 0
    for chapter in chapters:
        for section in chapter.sections.all():
            if section.content:
                total_word_count += len(section.content)

    if book.goal_word_count > 0:
        progress = int((total_word_count / book.goal_word_count) * 100)
        if progress > 100:
            progress = 100
    else:
        progress = 0

    return render(request, 'nbooks/book_detail.html', {
        'book': book,
        'chapters': chapters,
        'total_word_count': total_word_count,
        'progress': progress,
    })

@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_list')  # 책 목록 페이지로 이동 예정
    else:
        form = BookForm()
    return render(request, 'nbooks/create_book.html', {'form': form})
