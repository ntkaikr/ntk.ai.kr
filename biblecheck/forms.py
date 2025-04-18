from django import forms
from .models import BibleCheck

class BibleCheckForm(forms.ModelForm):
    class Meta:
        model = BibleCheck
        fields = ['book', 'chapter']
        widgets = {
            'book': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '예: 창세기'}),
            'chapter': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '예: 3'}),
        }
        labels = {
            'book': '성경',
            'chapter': '장',
        }
