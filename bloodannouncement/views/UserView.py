from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView

from ..models.user import User
from ..serializers.UserSerializer import UserSerializer, ChangePasswordSerializer, UserUpdateSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'pk'

    def get_object(self):
        if self.action == "partial_update":
            return self.request.user
        else:
            return super().get_object()

    def get_serializer_class(self):
        if self.action == "partial_update":
            return UserUpdateSerializer
        else:
            return UserSerializer


class ChangeUserPasswordView(APIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = request.user
            user.set_password(request.data['new_password'])
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
