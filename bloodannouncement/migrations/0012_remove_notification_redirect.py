# Generated by Django 3.1.3 on 2020-12-16 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodannouncement', '0011_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='redirect',
        ),
    ]
