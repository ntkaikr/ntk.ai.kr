# averager/forms.py
from django import forms

class AveragingForm(forms.Form):
    old_qty = forms.DecimalField(
        label="기존 수량",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'0'
        })
    )
    old_price = forms.DecimalField(
        label="기존 단가",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'0'
        })
    )
    new_qty = forms.DecimalField(
        label="추가 수량",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'0'
        })
    )
    new_price = forms.DecimalField(
        label="추가 단가",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'0'
        })
    )
