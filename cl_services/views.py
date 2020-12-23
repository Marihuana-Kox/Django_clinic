from django.shortcuts import render

from . models import ServicesAndPrice


def get_service_select(request, service):
    selected_service = ServicesAndPrice.objects.filter(disease__exact=service)
    return render(request, 'cl_calendar/empty.html', {'selected_service': selected_service,})