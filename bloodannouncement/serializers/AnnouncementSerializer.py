from rest_framework import serializers
from ..models.announcement import Announcement
from ..serializers.UserSerializer import UserSerializer


class AnnouncementSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Announcement
        fields = [
            'id',
            'description',
            'expiretion_time',
            'created_date',
            'phone_number',
            'hospital_address',
            'bload_group',
            'user'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user, context=self.context).data
        return data


class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = (
            'description',
            'expiretion_time',
            'phone_number',
            'hospital_address',
            'bload_group',
            'is_active'
        )
