# Generated by Django 3.1.7 on 2021-10-18 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 22, 14, 11, 353397)),
        ),
    ]
