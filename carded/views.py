from django.shortcuts import render, redirect, get_object_or_404
from .models import Card, SocialLink
from django.contrib.auth.decorators import login_required
from .forms import SocialLinkForm
from .utils import extract_favicon_url
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Card
from django.contrib.auth.models import User
from .forms import SocialLinkForm, CardImageForm  # ✅ 추가
from .models import Card, SocialLink, CardImage   # ✅ 추가

@login_required
def my_card_view(request):
    card, _ = Card.objects.get_or_create(user=request.user)

    social_form = SocialLinkForm()
    image_form = CardImageForm()

    if request.method == 'POST':
        if 'upload_image' in request.POST:
            image_form = CardImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                if card.images.count() >= card.image_limit():
                    image_form.add_error('image', f"{card.get_plan_display()} 요금제는 최대 {card.image_limit()}장의 이미지만 등록할 수 있습니다.")
                else:
                    img = image_form.save(commit=False)
                    img.card = card
                    img.save()
                    return redirect('carded:my_card')

        elif 'add_link' in request.POST:
            social_form = SocialLinkForm(request.POST)
            if social_form.is_valid():
                link = social_form.save(commit=False)
                link.card = card
                link.favicon_url = extract_favicon_url(link.url)
                try:
                    link.clean()
                    link.save()
                    return redirect('carded:my_card')
                except ValidationError as e:
                    social_form.add_error(None, e.message)

    return render(request, 'carded/my_card.html', {
        'card': card,
        'form': social_form,
        'image_form': image_form,
        'social_links': card.social_links.all(),
        'images': card.images.all(),
    })

def public_card_by_username(request, username):
    user = get_object_or_404(User, username=username)
    card = get_object_or_404(Card, user=user)
    return render(request, 'carded/card.html', {
        'card': card,
        'social_links': card.social_links.all()
    })

def card_view(request):
    card = get_object_or_404(Card, user=request.user)
    return render(request, 'carded/card.html', {
        'card': card,
        'social_links': card.social_links.all()
    })

@login_required
def delete_social_link(request, link_id):
    link = get_object_or_404(SocialLink, id=link_id, card__user=request.user)
    link.delete()
    return redirect('carded:my_card')
