# dailyq/forms.py
from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["child_name", "answer_text"]
        widgets = {
            "child_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "예: 민준"}),
            "answer_text": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "아이의 말/표현/상황을 간단히 적어주세요"}),
        }
