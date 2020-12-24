# Generated by Django 3.1.3 on 2020-12-16 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloodannouncement', '0010_announcement_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=['announcement', 'Announcement'], default='info', max_length=16)),
                ('redirect', models.URLField(blank=True, max_length=500, null=True)),
                ('announcement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bloodannouncement.announcement')),
                ('receiver_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('sender_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]