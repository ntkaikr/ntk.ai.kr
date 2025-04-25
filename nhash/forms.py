from django import forms

HASH_CHOICES = [
    ('md5','MD5'), ('sha1','SHA-1'),
    ('sha256','SHA-256'),
]

class HashForm(forms.Form):
    text = forms.CharField(label="원본 텍스트",
                           widget=forms.Textarea(attrs={'class':'form-control','rows':2}))
    algorithm = forms.ChoiceField(label="알고리즘",
                                  choices=HASH_CHOICES,
                                  widget=forms.Select(attrs={'class':'form-select'}))
