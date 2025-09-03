from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "image", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
    def clean_image(self):
        f = self.cleaned_data.get("image")
        if not f:
            raise ValidationError("이미지를 선택하세요.")
        # 확장자/콘텐츠 타입 제한 (JPG/PNG 추천)
        ok_ct = {"image/jpeg", "image/png"}
        if getattr(f, "content_type", None) not in ok_ct:
            raise ValidationError("JPG 또는 PNG 파일만 업로드할 수 있습니다.")
        if f.size > 5 * 1024 * 1024:
            raise ValidationError("이미지 최대 5MB까지 가능합니다.")
        return f

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "댓글을 입력하세요",
                "class": "form-control mb-2"
            }),
        }