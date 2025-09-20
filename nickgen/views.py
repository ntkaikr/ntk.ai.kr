# apps/nickgen/views.py
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .forms import GenerateForm
from .models import SavedNickname
from . import wordbank as wb
from . import nonsense as ns
from django.db import models

SESSION_KEY = 'nickgen_once'

def _generate_combo(params):
    style = params.get('style','tech')
    lang = params.get('lang','mix')
    seed = params.get('seed','')
    count = int(params.get('count', 12))
    min_len = int(params.get('min_len', 0))
    max_len = int(params.get('max_len', 16))
    allow_num = params.get('allow_number_tail', 'true') in ('true','1','on', True)

    out, seen, tries = [], set(), 0
    while len(out) < count and tries < count * 30:
        adj, nn = wb.pick(style, lang)
        candidate = wb.compose(adj, nn, seed=seed, tail_num=allow_num)
        c = candidate.replace('-', '').replace('_','')
        if not (min_len <= len(c) <= max_len):
            tries += 1; continue
        if any(b.lower() in candidate.lower() for b in wb.BAN):
            tries += 1; continue
        if candidate in seen:
            tries += 1; continue
        seen.add(candidate)
        out.append(candidate)
        tries += 1
    return out

def _generate_nonsense(params):
    lang = params.get('lang','mix')
    count = int(params.get('count', 12))
    min_len = int(params.get('min_len', 2))
    max_len = int(params.get('max_len', 10))
    seed = params.get('seed','')

    out = []
    for _ in range(count):
        if lang == 'ko':
            base = ns.gibberish_ko(2, 4)
        elif lang == 'en':
            base = ns.gibberish_en(max(3, min_len), min(10, max_len))
        else:
            base = ns.gibberish_ko(2, 3) + ns.gibberish_en(2, 6)
        if seed and len(base) + len(seed) <= max_len:
            base = f"{base}{seed}"
        out.append(base[:max_len])
    return out

def _generate_list(params):
    mode = params.get('mode','combo')
    return _generate_combo(params) if mode == 'combo' else _generate_nonsense(params)

@require_GET
def generator_view(request):
    if not request.user.is_authenticated and request.session.get(SESSION_KEY):
        return render(request, 'nickgen/limit.html')

    form = GenerateForm(request.GET or None)
    results = []
    if form.is_valid():
        results = _generate_list(form.cleaned_data)
        if not request.user.is_authenticated:
            request.session[SESSION_KEY] = True
    else:
        form = GenerateForm()

    return render(request, 'nickgen/generator.html', {'form': form, 'results': results})

@require_GET
def api_generate(request):
    data = _generate_list(request.GET)
    return JsonResponse({'results': data})

@require_POST
@login_required
def save_nickname(request):
    text = request.POST.get('text','')[:64]
    if not text:
        return HttpResponseBadRequest('no text')
    SavedNickname.objects.get_or_create(
        user=request.user,
        text=text,
        defaults={
            'style': request.POST.get('style',''),
            'lang': request.POST.get('lang',''),
            'seed': request.POST.get('seed','')
        }
    )
    return JsonResponse({'ok': True})

@require_POST
@login_required
def copy_ping(request):
    text = request.POST.get('text','')[:64]
    if not text:
        return HttpResponseBadRequest('no text')
    SavedNickname.objects.filter(user=request.user, text=text).update(
        copied_count=models.F('copied_count') + 1
    )
    return JsonResponse({'ok': True})

# apps/nickgen/views.py  (하단에 추가)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def my_nicknames(request):
    qs = SavedNickname.objects.filter(user=request.user).only(
        "text", "created_at", "copied_count", "style", "lang", "seed"
    )
    pg = Paginator(qs, 20)
    page = pg.get_page(request.GET.get("page"))
    return render(request, "nickgen/my_nicknames.html", {"page": page})
