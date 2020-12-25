from django.db import models
from cl_medication.models import DiagnosSelect, MedicationServices


class SelectMedication(models.Model):
    diagnos = models.ForeignKey(
        DiagnosSelect, on_delete=models.CASCADE, verbose_name='Диагноз')
    medication = models.ForeignKey(
        MedicationServices, on_delete=models.CASCADE, verbose_name='Лечение')

    def __str__(self):
        return self.diagnos


class RecordPacientDate(models.Model):
    """Запись пациентов по времени и дате"""
    phone = models.CharField(default=0, max_length=20, verbose_name='Телефон')
    surname = models.CharField(
        max_length=20, blank=True, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    patronymic = models.CharField(
        max_length=20, blank=True,  verbose_name='Отчество')
    dob = models.DateField(default=0, max_length=10, blank=True,
                           verbose_name='Дата рождения')
    curent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
