# Generated by Django 3.0 on 2020-12-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('dob', models.DateField()),
            ],
        ),
    ]