from django import forms
from . models import SelectMedication, RecordPacientDate


class SelectMedicationForm(forms.ModelForm):
    class Meta:
        model = SelectMedication
        fields = ['diagnos', 'medication']
        widgets = {
            'diagnos': forms.Select(attrs={'title': 'Выберите проблемный вопрос', 'autofocus': True}),
            'medication': forms.Select(attrs={'disabled': 'disabled'}),
        }
