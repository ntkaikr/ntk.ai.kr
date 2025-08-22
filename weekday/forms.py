# weekday/forms.py
from django import forms

class WeekdayForm(forms.Form):
    date = forms.DateField(
        label="날짜",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
