# Generated by Django 3.1.3 on 2020-12-17 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloodannouncement', '0016_auto_20201217_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
