from django.shortcuts import render
from . models import MedicationServices

def get_service_select(request, medications):
    selected_service = MedicationServices.objects.filter(diagnos__exact=medications)
    return render(request, 'cl_medication/select.html', {'selected_service': selected_service,})
