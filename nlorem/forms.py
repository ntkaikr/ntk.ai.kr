from django import forms

class LoremForm(forms.Form):
    paragraphs = forms.IntegerField(
        label="문단 수",
        min_value=1, max_value=10, initial=3,
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )
