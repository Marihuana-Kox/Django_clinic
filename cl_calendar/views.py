from django.shortcuts import render, get_object_or_404
from django.template import Context, Template, loader
from datetime import datetime as dt
from django.http import HttpResponse, HttpResponseNotFound
from . custom_calendar import calendar_best as cal
from . models import RegistrationDate, WorkinDays
from . forms import RegistrationDateForm


def index(request):
    form = RegistrationDateForm()
    week_work = WorkinDays.objects.all()
    now = dt.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    calendarius = cal(year, month, week_work)
    return render(request, 'cl_calendar/index.html',
                  {'calendarius': calendarius, 'form': form})


def get_month(request, year, month):
    week_work = WorkinDays.objects.all()
    calendarius = cal(year, month, week_work)
    return render(request, 'cl_calendar/index.html',
                  {'calendarius': calendarius, })


def add_register(request, regdate):
    form = RegistrationDateForm()
    template = loader.get_template('cl_calendar/modal_form.html')
    if regdate not in 'undefined':
        context = {
            'regdate': regdate,
            'form': form,
        }
        # html = "<div class='regDate'><h3> %s </h3>'{% form %}'</div>" % regdate
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("<div class='regDate'><h3>Нет страницы</h3></div>")
