from django.contrib import admin
# Register your models here.
from . models import RegistrationDate


class RegistrationDateAdmin(admin.ModelAdmin):
    list_display = ('phone', 'surname', 'name', 'patronymic', 'dob')
    search_fields = ('phone', 'surname', 'dob')


admin.site.register(RegistrationDate, RegistrationDateAdmin)
