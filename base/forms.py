from django import forms
from .models import Vacation


class AddCVacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ('start', 'end', 'many')
        widgets = {
            'many': forms.NumberInput()
        }
        error_messages = {
            'many': {
                'required': 'این فیلد اجباری است',
            }
        }
        help_texts = {
            'many': 'max 400 char'
        }
        labels = {
            'start': 'تاریخ شروع',
            'end': 'تاریخ شروع',
            'many': 'تاریخ شروع',

        }
