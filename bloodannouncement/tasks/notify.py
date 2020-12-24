import dramatiq
from ..models.user import User
from ..serializers.NotificationSerializer import NotificationSerializer

__all__ = ['create_notifications']

@dramatiq.actor
def create_notifications(request, announcement_id):
    users = User.objects.all()
    for user in users:
        notification_data = {
            "receiver_user": user.pk,
            "announcement": announcement_id
        }
        notification_serializer = NotificationSerializer(data=notification_data, context={'request': request})
        notification_serializer.is_valid(raise_exception=True)
        notification_serializer.save()