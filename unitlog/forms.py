from django import forms
from .models import Residence

class ResidenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        fields = ["floor", "room_number", "resident", "note"]
        widgets = {
            "floor": forms.NumberInput(attrs={"class": "form-control"}),
            "room_number": forms.TextInput(attrs={"class": "form-control"}),
            "resident": forms.TextInput(attrs={"class": "form-control"}),
            "note": forms.TextInput(attrs={"class": "form-control"}),
        }
