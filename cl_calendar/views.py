from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
import calendar
from .custom_calendar import Custom_calendar as cal

# Create your views here.


def index(request):
    months = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель", 
            5: "Май", 
            6: "Июнь", 
            7: "Июль", 
            8: "Август", 
            9: "Сентябрь", 
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь",
            }
    k = cal("Хуйня")
    c = calendar.HTMLCalendar()
    html_out = c.formatmonth(dt.today().year, dt.today().month)
    now = dt.now()
    times = now.strftime("%H:%M:%S")
    date = now.strftime("%Y:%m:%d  %U")
    today = dt.today()
    today = today.strftime("%d")
    m = now.strftime("%m")
    month = months[int(m)]
    return render(request, 'cl_calendar/index.html',
                  {'today': today, 'month': month, 'date': date, 'times': times, 'html_out': html_out, 'k': k})
