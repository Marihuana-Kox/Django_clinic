from django.contrib import admin
# Register your models here.
from . models import WorkinDays, Week


class WeekAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


class WorkinDaysAdmin(admin.ModelAdmin):
    list_display = ('time_work', 'time_doctor', 'happy_days')


admin.site.register(Week, WeekAdmin)
admin.site.register(WorkinDays, WorkinDaysAdmin)
