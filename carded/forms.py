from django import forms
from .models import SocialLink
from .models import CardImage

class CardImageForm(forms.ModelForm):
    class Meta:
        model = CardImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['label', 'url']
        widgets = {
            'label': forms.TextInput(attrs={
                'placeholder': '예: GitHub',
                'class': 'form-control',
            }),
            'url': forms.URLInput(attrs={
                'placeholder': 'https://github.com/username',
                'class': 'form-control',
            }),
        }
