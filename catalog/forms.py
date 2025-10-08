from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["name", "contact", "quantity"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ваше имя", "required": True}),
            "contact": forms.TextInput(attrs={"placeholder": "Email или телефон", "required": True}),
            "quantity": forms.NumberInput(attrs={"min": 1, "value": 1}),
        }
