from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortLink
from .forms import ShortLinkForm

def link_create(request):
    if request.method == 'POST':
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            short_link = form.save()
            return render(request, 'linkn/link_created.html', {'short_link': short_link})
    else:
        form = ShortLinkForm()
    return render(request, 'linkn/link_create.html', {'form': form})

def redirect_short_link(request, slug):
    link = get_object_or_404(ShortLink, slug=slug)
    link.click_count += 1
    link.save()
    return redirect(link.original_url)
