from django.db import models

# Create your models here.


class SelectTerm(models.Model):
    class Meta:
        verbose_name_plural = 'Срок'

    term = models.FloatField(default=0.0, verbose_name='Год')

    def __str__(self):
        return " %s " % self.term


class SelectADisease(models.Model):
    class Meta:
        verbose_name_plural = 'Диагноз'

    disease = models.CharField(max_length=100, verbose_name='Диагноз')

    def __str__(self):
        return self.disease


class ServicesAndPrice(models.Model):
    class Meta:
        verbose_name_plural = 'Услуги и цены'

    disease = models.ForeignKey(SelectADisease, default=0, on_delete=models.CASCADE, related_name='diagnos')
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')
    price = models.FloatField(default=0.00, verbose_name='Стоимость услуги')
    time_work = models.FloatField(max_length=5, default=1.00, verbose_name='Время процедуры')
    term = models.ForeignKey(SelectTerm, default=0, on_delete=models.CASCADE, related_name='termcod')

    def __str__(self):
        return self.name
