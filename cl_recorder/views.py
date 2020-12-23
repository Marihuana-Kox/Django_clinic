from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView
from . models import RecordPacientDate
from . forms import SelectMedicationForm


class IndexRecorderView(ListView):
    """Страница записи пациентов"""
    model = RecordPacientDate
    template_name = 'cl_recorder/index.html'

    def get(self, request):
        form = SelectMedicationForm()
        return render(request, self.template_name, {'form': form})