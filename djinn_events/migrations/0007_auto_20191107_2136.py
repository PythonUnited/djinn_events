# Generated by Django 2.0.13 on 2019-11-07 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djinn_events', '0006_auto_20191022_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Start date'),
        ),
    ]