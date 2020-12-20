from django.contrib import admin

from .models import *


class SelectTermAdmin(admin.ModelAdmin):
    list_display = ('term',)


class SelectADiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease',)


class ServicesAndPriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(SelectTerm, SelectTermAdmin)
admin.site.register(SelectADisease, SelectADiseaseAdmin)
admin.site.register(ServicesAndPrice, ServicesAndPriceAdmin)
