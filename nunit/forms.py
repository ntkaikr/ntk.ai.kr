from django import forms

UNIT_CHOICES = [
    ('km_m','km → m'), ('m_km','m → km'),
    ('kg_g','kg → g'), ('g_kg','g → kg'),
    ('c_f','℃ → ℉'), ('f_c','℉ → ℃'),
]

class UnitForm(forms.Form):
    value = forms.FloatField(label="값", widget=forms.NumberInput(attrs={'class':'form-control'}))
    conversion = forms.ChoiceField(label="변환", choices=UNIT_CHOICES,
                                   widget=forms.Select(attrs={'class':'form-select'}))
