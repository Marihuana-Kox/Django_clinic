from django.db import models
from cl_services.models import SelectADisease, ServicesAndPrice


class Week(models.Model):
    class Meta:
        verbose_name_plural = 'Дни недели'

    name = models.CharField(
        max_length=12, default='Понедельник', verbose_name='День')
    number = models.IntegerField(default=0, verbose_name='Номер')

    def __str__(self):
        return self.name


class WorkinDays(models.Model):
    class Meta:
        verbose_name_plural = 'Рабочие дни'

    time_work = models.CharField(max_length=50, verbose_name='Рабочие часы')
    time_doctor = models.CharField(max_length=50, verbose_name='Прием врача')
    week_day = models.ManyToManyField(
        Week, verbose_name='Рабочие дни', default='')
    happy_days = models.CharField(max_length=150, verbose_name='Выходные дни', blank=True)

    def __str__(self):
        return 'Установка рабочего времени'


class RegistrationDate(models.Model):
    class Meta:
        verbose_name_plural = 'Запись к врачу'
        
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    dob = models.DateField(max_length=10, verbose_name='Дата рождения')
    disease = models.ForeignKey(SelectADisease, on_delete=models.CASCADE, default=0, related_name='selects', verbose_name='Диагноз')
    service_diagnos = models.ForeignKey(ServicesAndPrice, on_delete=models.CASCADE, default=0)
    curent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
