from django import forms
from .models import Tool
# toolhub/forms.py
from .models import Comment, Reply
# toolhub/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'stars']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': '댓글을 입력하세요...',
                'class': 'form-control'
            }),
            'stars': forms.RadioSelect(choices=[
                (5, '⭐⭐⭐⭐⭐'),
                (4, '⭐⭐⭐⭐'),
                (3, '⭐⭐⭐'),
                (2, '⭐⭐'),
                (1, '⭐'),
            ])
        }
        labels = {
            'content': '',  # 라벨 제거
            'stars': '별점 평가'
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '대댓글 입력'}),
        }

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description', 'visibility', 'access_level', 'allowed_level', 'allowed_users', 'link', 'thumbnail']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-select'}),
            'access_level': forms.Select(attrs={'class': 'form-select'}),
            'allowed_level': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '숫자 입력'}),
            'allowed_users': forms.SelectMultiple(attrs={'class': 'form-select', 'size': 4}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': '예: http://www.ntk.ai.kr/yourtool'}),
        }
