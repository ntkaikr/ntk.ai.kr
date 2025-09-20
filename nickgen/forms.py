# apps/nickgen/forms.py
from django import forms

STYLE_CHOICES = [
    ('cute','귀염'), ('tech','개발자'), ('sage','고전'), ('myth','신화'), ('city','도시')
]
LANG_CHOICES = [('ko','한글'), ('en','영문'), ('mix','혼합')]
MODE_CHOICES = [('combo','의미 있는 조합'), ('nonsense','무의미 생성')]

class GenerateForm(forms.Form):
    mode = forms.ChoiceField(choices=MODE_CHOICES, initial='combo', widget=forms.Select(attrs={'class':'form-select'}))
    style = forms.ChoiceField(choices=STYLE_CHOICES, initial='tech', required=False, widget=forms.Select(attrs={'class':'form-select'}))
    lang = forms.ChoiceField(choices=LANG_CHOICES, initial='mix', widget=forms.Select(attrs={'class':'form-select'}))
    seed = forms.CharField(required=False, max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'예: kid, star'}))
    count = forms.IntegerField(min_value=1, max_value=50, initial=12, widget=forms.NumberInput(attrs={'class':'form-control'}))
    min_len = forms.IntegerField(min_value=0, max_value=20, initial=0, widget=forms.NumberInput(attrs={'class':'form-control'}))
    max_len = forms.IntegerField(min_value=1, max_value=32, initial=16, widget=forms.NumberInput(attrs={'class':'form-control'}))
    allow_number_tail = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
