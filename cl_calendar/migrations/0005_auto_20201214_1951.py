# Generated by Django 3.0 on 2020-12-14 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_services', '0005_servicesandprice_time_work'),
        ('cl_calendar', '0004_auto_20201214_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdate',
            name='selectservices',
        ),
        migrations.AddField(
            model_name='registrationdate',
            name='diagnos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='selects', to='cl_services.SelectADisease', verbose_name='Диагноз'),
        ),
    ]
