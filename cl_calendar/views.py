from django.shortcuts import render
from datetime import datetime as dt
from .custom_calendar import calendar_best as cal
# Create your views here.


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

