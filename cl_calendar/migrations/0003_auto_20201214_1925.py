# Generated by Django 3.0 on 2020-12-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_services', '0005_servicesandprice_time_work'),
        ('cl_calendar', '0002_auto_20201214_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectservices',
            name='disease',
        ),
        migrations.AddField(
            model_name='selectservices',
            name='disease',
            field=models.ManyToManyField(to='cl_services.SelectADisease'),
        ),
        migrations.AlterField(
            model_name='workindays',
            name='happy_days',
            field=models.CharField(blank=True, max_length=150, verbose_name='Выходные дни'),
        ),
    ]