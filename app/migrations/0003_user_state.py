# Generated by Django 3.2.3 on 2021-07-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_xray_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='punjab', max_length=450),
        ),
    ]