from django import forms

class RandomForm(forms.Form):
    min_value = forms.IntegerField(label="최소값", initial=1)
    max_value = forms.IntegerField(label="최대값", initial=100)
    count     = forms.IntegerField(label="생성 개수", min_value=1, initial=1)
