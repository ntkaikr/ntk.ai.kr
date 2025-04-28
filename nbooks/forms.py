from django import forms
from .models import Book
from .models import Chapter
from .models import Section

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '섹션 제목'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': '여기에 글을 쓰세요...'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '섹션 순서'}),
        }

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '챕터 제목 입력'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '챕터 순서'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'goal_word_count', 'is_public']  # is_public 추가
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '책 제목을 입력하세요'}),
            'goal_word_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '목표 글자 수'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }