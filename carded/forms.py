from django import forms
from .models import SocialLink

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['label', 'url']
        widgets = {
            'label': forms.TextInput(attrs={'placeholder': '예: GitHub'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://github.com/username'}),
        }
