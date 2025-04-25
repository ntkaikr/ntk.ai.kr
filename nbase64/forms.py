from django import forms

class Base64Form(forms.Form):
    text = forms.CharField(
        label="인코드/디코드할 텍스트",
        widget=forms.Textarea(attrs={'class':'form-control','rows':3})
    )
    action = forms.ChoiceField(
        label="동작 선택",
        choices=[('encode','인코드'),('decode','디코드')],
        widget=forms.Select(attrs={'class':'form-select'})
    )
