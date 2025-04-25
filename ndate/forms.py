from django import forms
from .models import DDay

class DDayForm(forms.ModelForm):
    class Meta:
        model = DDay
        fields = ['target_date', 'title']
        widgets = {
            'target_date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'title':       forms.TextInput(attrs={'class':'form-control', 'placeholder':'제목 또는 설명'}),
        }
        labels = {
            'target_date': '날짜',
            'title':       '제목/설명',
        }
