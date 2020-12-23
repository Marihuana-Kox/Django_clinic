from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, Template, loader
from datetime import datetime as dt
from django.http import HttpResponse, HttpResponseNotFound
from . custom_calendar import calendar_best as cal
from . models import RegistrationDate, WorkinDays
from . forms import RegistrationDateForm


def index(request):
    """ Главная страница с текущим месяцем в календаре """
    form = RegistrationDateForm()
    week_work = WorkinDays.objects.all()
    now = dt.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    calendarius = cal(year, month, week_work)
    return render(request, 'cl_calendar/index.html',
                  {'calendarius': calendarius, 'form': form})


def get_month(request, year, month):
    """Метод формирует ссылки на другие месяца"""
    week_work = WorkinDays.objects.all()
    calendarius = cal(year, month, week_work)
    return render(request, 'cl_calendar/index.html',
                  {'calendarius': calendarius, })


def add_register(request):
    """Запись нового пациента на выбранную дату"""
    if request.method == 'POST':
        form = RegistrationDateForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect("/")
        else:
            form = RegistrationDate()
            context = {'form': form,}
        return render(request, 'cl_calendar/index.html',
                  context)

