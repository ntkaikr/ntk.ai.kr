from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import BibleCheck
from .constants import BIBLE_STRUCTURE
from datetime import datetime, time, timedelta

@login_required
def check(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)

    today_qs = BibleCheck.objects.filter(
        user=request.user,
        date__gte=datetime.combine(today, datetime.min.time()),
        date__lt=datetime.combine(tomorrow, datetime.min.time())
    ).order_by('-date', '-id')

    selected = {
        'testament': request.POST.get('testament'),
        'section': request.POST.get('section'),
        'book': request.POST.get('book'),
    }

    context = {
        'structure': BIBLE_STRUCTURE,
        'selected': selected,
        'selected_chapters': [],
        'today_records': list(today_qs),
        'sections': [],
        'available_books': {},
        'max_chapter': None,
        'already_checked': [],
    }

    # ✅ 역탐색: book만 넘어온 경우 상위 구조 보완
    if selected['book'] and not (selected['testament'] and selected['section']):
        for testament, sections in BIBLE_STRUCTURE.items():
            for section, books in sections.items():
                if selected['book'] in books:
                    selected['testament'] = testament
                    selected['section'] = section
                    break
            if selected['testament']:
                break

    # 1️⃣ 구약/신약
    if selected['testament'] in BIBLE_STRUCTURE:
        context['sections'] = list(BIBLE_STRUCTURE[selected['testament']].keys())

        # 2️⃣ 분류
        if selected['section'] in BIBLE_STRUCTURE[selected['testament']]:
            books_dict = BIBLE_STRUCTURE[selected['testament']][selected['section']]
            context['available_books'] = books_dict

            # 3️⃣ 성경
            if selected['book'] in books_dict:
                context['max_chapter'] = books_dict[selected['book']]

                start = datetime.combine(date.today(), time.min)
                end = datetime.combine(date.today(), time.max)

                # ✅ 장 체크한 기록
                qs = BibleCheck.objects.filter(
                    user=request.user,
                    book=selected['book'],
                    date__range=(start, end)  # ✅ 시간 범위로 안전하게 처리
                    #date__date=date.today()
                )

                context['already_checked'] = [str(ch) for ch in qs.values_list('chapter', flat=True)]
                #context['today_records'] = list(qs)

    # 4️⃣ 체크 제출 처리
    if request.method == 'POST':
        chapters = request.POST.getlist('chapters')
        book = selected['book']

        if book and chapters:
            start = datetime.combine(date.today(), time.min)
            end = datetime.combine(date.today(), time.max)

            already_chapters = set(BibleCheck.objects.filter(
                user=request.user,
                book=book,
                date__range=(start, end)
            ).values_list('chapter', flat=True))

            for ch in chapters:
                if int(ch) not in already_chapters:
                    BibleCheck.objects.create(
                        user=request.user,
                        book=book,
                        chapter=int(ch),
                        date=datetime.now()
                    )

            return redirect('biblecheck:check')

        context['selected_chapters'] = chapters

    return render(request, 'biblecheck/check.html', context)

@login_required
def index(request):
    return redirect('biblecheck:check')

@login_required
def history(request):
    records = BibleCheck.objects.filter(user=request.user).order_by('-date', '-id')
    return render(request, 'biblecheck/history.html', {
        'records': records
    })
