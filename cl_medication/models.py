from django.db import models


class DiagnosSelect(models.Model):
    """Диагноз"""
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Диагноз'


class MedicationServices(models.Model):
    """Методы лечения, зависимы от выбора - Диагноз"""
    diagnos = models.ForeignKey(
        DiagnosSelect, on_delete=models.CASCADE, verbose_name='Диагноз')
    name = models.CharField(blank=True, max_length=150,
                            verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    term = models.FloatField(default=0.00, verbose_name='Срок кадирования')
    time_work = models.TimeField(default=00.00, verbose_name='Время работы')
    price = models.FloatField(default=0.00, verbose_name='Стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Лечение'
