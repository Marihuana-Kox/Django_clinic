from django import forms
from django.utils.translation import gettext_lazy as _
from cl_calendar.models import RegistrationDate


class RegistrationDateForm(forms.ModelForm):
    class Meta:
        model = RegistrationDate
        fields = ['disease', 'service_diagnos', 'phone', 'surname', 'name', 'patronymic', 'dob']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+7'}),
            'diagnos': forms.Select(attrs={'title': 'Выберите проблемный вопрос'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'maxlength': 10}),
            'service_diagnos': forms.Select(attrs={'disabled': 'disabled'}),
        }