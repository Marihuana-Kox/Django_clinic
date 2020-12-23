from django.contrib import admin

from . models import DiagnosSelect, MedicationServices


class DiagnosSelectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class MedicationServicesAdmin(admin.ModelAdmin):
    list_display = ('diagnos', 'name', 'description', 'term', 'time_work', 'price')


admin.site.register(DiagnosSelect, DiagnosSelectAdmin)
admin.site.register(MedicationServices, MedicationServicesAdmin)
