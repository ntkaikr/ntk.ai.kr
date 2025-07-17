from django import forms
from .models import Script
from .models import Character
from .models import Scene
from .models import Dialogue

class DialogueForm(forms.ModelForm):
    class Meta:
        model = Dialogue
        fields = ['character', 'line']
        widgets = {
            'character': forms.Select(attrs={'class': 'form-control'}),
            'line': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': '대사를 입력하세요'}),
        }

    def __init__(self, *args, **kwargs):
        script = kwargs.pop('script', None)  # script 인자를 꺼냄
        super().__init__(*args, **kwargs)

        if script:
            self.fields['character'].queryset = Character.objects.filter(script=script)


class SceneForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = ['title', 'location', 'time_of_day', 'mood', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '씬 제목'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '장소 (예: 카페)'}),
            'time_of_day': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '시간 (예: 오후 3시)'}),
            'mood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '분위기 (예: 긴장감)'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름 (예: 민준)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': '간단한 설명 (예: 차가운 성격의 형사)'}),
        }

class ScriptForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '대본 제목'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '간단한 설명'}),
        }


