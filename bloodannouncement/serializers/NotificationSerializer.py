from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..serializers.UserSerializer import UserSerializer
from ..models.notification import Notification
from ..models.announcement import Announcement
from ..serializers.AnnouncementSerializer import AnnouncementSerializer

User = get_user_model()


class NotificationSerializer(serializers.ModelSerializer):
    sender_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    receiver_user_detail = UserSerializer(source='receiver_user', many=False, read_only=True, required=False)
    receiver_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(), allow_null=True, allow_empty=True)
    announcement = serializers.PrimaryKeyRelatedField(queryset=Announcement.objects.filter(), allow_empty=True, allow_null=True)

    class Meta:
        model = Notification
        fields = (
            'sender_user',
            'receiver_user',
            'receiver_user_detail',
            'notification_type',
            'announcement',
            'notification_type'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['announcement'] = AnnouncementSerializer(instance.announcement, context=self.context).data
        return data