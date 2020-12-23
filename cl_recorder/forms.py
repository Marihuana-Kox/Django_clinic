from django import forms
from . models import SelectMedication, RecordPacientDate


class SelectMedicationForm(forms.ModelForm):
    class Meta:
        model = SelectMedication
        fields = ['diagnos', 'medication']
