from django import forms

class PasswordForm(forms.Form):
    length = forms.IntegerField(
        label='비밀번호 길이',
        min_value=4,
        max_value=128,
        initial=12,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '예: 12'
        })
    )
    use_letters    = forms.BooleanField(
        label='영문자 포함', required=False, initial=True,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input'})
    )
    use_digits     = forms.BooleanField(
        label='숫자 포함',   required=False, initial=True,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input'})
    )
    use_punctuation = forms.BooleanField(
        label='특수문자 포함', required=False, initial=True,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input'})
    )
