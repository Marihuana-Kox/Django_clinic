from django.contrib import admin
# Register your models here.
from . models import RegistrationDate, WorkinDays, Week


class WeekAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')



class RegistrationDateAdmin(admin.ModelAdmin):
    list_display = ('phone', 'surname', 'name', 'patronymic', 'dob')
    search_fields = ('phone', 'surname', 'dob')



class WorkinDaysAdmin(admin.ModelAdmin):
    list_display = ('time_work', 'time_doctor', 'happy_days')


admin.site.register(Week, WeekAdmin)
admin.site.register(RegistrationDate, RegistrationDateAdmin)
admin.site.register(WorkinDays, WorkinDaysAdmin)
