from django import forms

class CountForm(forms.Form):
    content = forms.CharField(
        label="텍스트 입력",
        widget=forms.Textarea(attrs={
            'class':'form-control','rows':4,
            'placeholder':'텍스트를 붙여넣으세요...'
        })
    )
