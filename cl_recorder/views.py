from django.shortcuts import render
from datetime import datetime as dt
# from django.http import HttpResponse, HttpResponseNotFound
from . custom_calendar import calendar_best as cal
from . record_work_day import free_days_week as fdw
# from django.views.generic import ListView, TemplateView, FormView
from . models import RecordPacientDate
from . forms import SelectMedicationForm

from cl_calendar.models import WorkinDays
from cl_medication.models import DiagnosSelect, MedicationServices


def index_select_diagnos(request):
    form = SelectMedicationForm
    work_time = WorkinDays.objects.all()
    now = dt.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    calendarius = cal(year, month, work_time)
    template_name = 'cl_recorder/index.html'
    return render(request, template_name, {'calendarius': calendarius, 'form': form, 'work_time': work_time})


def get_month(request, year, month):
    """Метод формирует ссылки на другие месяца"""
    work_time = WorkinDays.objects.all()
    calendarius = cal(year, month, work_time)
    template_name = 'cl_recorder/calendar_empty.html'
    return render(request, template_name, {'calendarius': calendarius, 'work_time': work_time})


def get_free_date_time(request, day, month, year, medic):
    """ Главная страница с текущим месяцем в календаре """
    work_time = WorkinDays.objects.all()
    medical = MedicationServices.objects.get(pk=medic)
    record_day = fdw(day, month, year, medical, work_time)
    context = {
        'record_day': record_day,
    }
    template_name = 'cl_recorder/record_free_time.html'
    return render(request, template_name, context)

# class IndexRecorderView(ListView):
#     """Страница записи пациентов"""
#     model = RecordPacientDate
#     template_name = 'cl_recorder/index.html'

#     def get(self, request):
#         form = SelectMedicationForm()
#         return render(request, self.template_name, {'form': form})
