from django.db import models
from django.contrib.auth import get_user_model
from ..models.announcement import Announcement

User = get_user_model()


class Notification(models.Model):
    notification_types = (
        ("announcement", "Announcement")
    )
    notification_type = models.CharField(max_length=16, choices=notification_types, default='info')
    receiver_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    sender_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.announcement
