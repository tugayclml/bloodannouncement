# Generated by Django 3.1.3 on 2020-12-17 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bloodannouncement', '0014_auto_20201217_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 0, 0, 1, 98049, tzinfo=utc)),
        ),
    ]
