# Generated by Django 3.1.7 on 2021-10-18 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211018_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 22, 32, 10, 766108)),
        ),
    ]