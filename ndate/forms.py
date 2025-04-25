from django import forms
from .models import DDay

class DDayForm(forms.ModelForm):
    class Meta:
        model = DDay
        fields = ['target_date']
        widgets = {
            'target_date': forms.DateInput(attrs={'type':'date','class':'form-control'})
        }
        labels = {'target_date': '목표 날짜'}
