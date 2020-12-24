# Generated by Django 3.1.3 on 2020-12-16 23:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloodannouncement', '0012_remove_notification_redirect'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2020, 12, 16, 23, 7, 32, 742954, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
