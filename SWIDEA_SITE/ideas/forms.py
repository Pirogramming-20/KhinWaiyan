# forms.py
from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('__all__')
        widgets = {
            'interest': forms.NumberInput(attrs={'min': 0}),  # Ensures the interest cannot go below 0
        }
