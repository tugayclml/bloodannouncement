# Generated by Django 3.1.3 on 2020-12-15 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodannouncement', '0008_auto_20201215_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='created_date',
        ),
    ]