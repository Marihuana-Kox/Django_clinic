from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
import calendar

# Create your views here.
def index(request):
    c = calendar.HTMLCalendar()
    html_out = c.formatmonth(dt.today().year, dt.today().month)
    now = dt.now()
    times = now.strftime("%H:%M:%S")
    return render(request, 'cl_calendar/index.html', {'times': times, 'html_out': html_out,})
