from django.db import models
from ..models.user import User
from django.utils import timezone


class Announcement(models.Model):
    description = models.CharField(max_length=1024)
    expiretion_time = models.DateField()
    bload_group = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    hospital_address = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description
