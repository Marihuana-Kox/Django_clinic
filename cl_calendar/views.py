from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt
from django.http import HttpResponse, HttpResponseNotFound
from .custom_calendar import calendar_best as cal
from .models import RegistrationDate


def index(request):
    now = dt.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    calendarius = cal(year, month)
    return render(request, 'cl_calendar/index.html',
                  {'calendarius': calendarius, })


def get_month(request, year, month):
    calendarius = cal(year, month)
    return render(request, 'cl_calendar/index.html',
                  {'calendarius': calendarius, })

def add_register(request, regdate):
    if regdate not in 'undefined':
        html = "<div class='regDate'><h3> %s </h3></div>" % regdate
        return HttpResponse(html)
    else:
        return HttpResponse("<div class='regDate'><h3>Нет страницы</h3></div>")