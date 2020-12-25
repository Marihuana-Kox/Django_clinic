from django.shortcuts import render
from datetime import datetime as dt
# from django.http import HttpResponse, HttpResponseNotFound
from . custom_calendar import calendar_best as cal
# from django.views.generic import ListView, TemplateView, FormView
from . models import RecordPacientDate
from . forms import SelectMedicationForm

from cl_calendar.models import WorkinDays
from cl_medication.models import DiagnosSelect, MedicationServices


def index_select_diagnos(request):
    form = SelectMedicationForm
    week_work = WorkinDays.objects.all()
    now = dt.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    calendarius = cal(year, month, week_work)
    template_name = 'cl_recorder/index.html'
    return render(request, template_name, {'calendarius': calendarius, 'form': form})


def get_month(request, year, month):
    """Метод формирует ссылки на другие месяца"""
    week_work = WorkinDays.objects.all()
    calendarius = cal(year, month, week_work)
    template_name = 'cl_recorder/calendar_empty.html'
    return render(request, template_name, {'calendarius': calendarius,})


def get_free_date_time(request, day, mont, year, medic):
    """ Главная страница с текущим месяцем в календаре """
    # form = RegistrationDateForm()
    # work_time = WorkinDays.objects.filter(week_day__in=day)
    work_time = f"Все успешно получилось {day} {mont} {year}" 
    # now = dt.now()
    # year = now.strftime('%Y')
    # month = now.strftime('%m')
    # calendarius = cal(year, month, week_work)
    template_name = 'cl_recorder/record_free_time.html'
    return render(request, template_name, {'work_time': work_time,})

# class IndexRecorderView(ListView):
#     """Страница записи пациентов"""
#     model = RecordPacientDate
#     template_name = 'cl_recorder/index.html'

#     def get(self, request):
#         form = SelectMedicationForm()
#         return render(request, self.template_name, {'form': form})
