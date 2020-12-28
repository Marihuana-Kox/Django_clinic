from django.db import models
from cl_medication.models import DiagnosSelect, MedicationServices


class RecordDate(models.Model):
    """Бронирование даты и времени приема"""
    datetime_record = models.DateTimeField(verbose_name='Дата и время записи пациента')

    def __str__(self):
        return self.datetime_record


class SelectMedication(models.Model):
    """Запись диагноза и метода лечения выбранного пациентом"""
    diagnos = models.ForeignKey(
        DiagnosSelect, on_delete=models.CASCADE, verbose_name='Диагноз')
    medication = models.ForeignKey(
        MedicationServices, on_delete=models.CASCADE, verbose_name='Лечение')

    def __str__(self):
        return self.diagnos


class RecordPacientDate(models.Model):
    """Запись пациентов данных пациентов"""
    
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

