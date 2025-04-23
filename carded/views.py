from django.shortcuts import render, redirect, get_object_or_404
from .models import Card, SocialLink
from django.contrib.auth.decorators import login_required
from .forms import SocialLinkForm
from .utils import extract_favicon_url

@login_required
def my_card_view(request):
    card, _ = Card.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.card = card
            link.favicon_url = extract_favicon_url(link.url)
            link.clean()  # SNS 개수 제한 체크
            link.save()
            return redirect('carded:my_card')

    else:
        form = SocialLinkForm()

    return render(request, 'carded/my_card.html', {
        'card': card,
        'form': form,
        'social_links': card.social_links.all()
    })
