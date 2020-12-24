from rest_framework import serializers
from ..models.user import User
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'surname',
            'phone_number',
            'bload_group',
            'email',
            'username',
            'password',
            'profile_picture',
            'is_active'
        )

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            bload_group=self.validated_data['bload_group'],
            profile_picture=self.validated_data['profile_picture']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'surname',
            'phone_number',
            'bload_group',
            'email',
            'profile_picture',
            'is_active'
        )


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        fields = ("old_password", "new_password")

    def validated_old_password(self, old_password):
        request = self.context.get("request")
        user = request.user
        valid_password = user.check_password(old_password)
        if not valid_password:
            raise ValidationError("Current password is wrong!")
        return old_password