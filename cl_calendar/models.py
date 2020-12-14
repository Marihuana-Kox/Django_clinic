from django.db import models
# Create your models here.


# class WorkinDate(models.Model):
#     class Meta:
#         verbose_name_plural = 'Предварительная запись'
#     date = models.DateField(verbose_name='Дата приема')
#     time = models.TimeField(verbose_name='Время')

#     def __str__(self):
#         return self.date


class RegistrationDate(models.Model):
    class Meta:
        verbose_name_plural = 'Запись к врачу'
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    dob = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.phone
