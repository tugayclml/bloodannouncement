from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from ..models.announcement import Announcement
from ..serializers.AnnouncementSerializer import AnnouncementSerializer, AnnouncementUpdateSerializer
from ..tasks.notify import create_notifications


class AnnouncementListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer

    def create(self, request, *args, **kwargs):
        announcement_serializer = AnnouncementSerializer(data=request.data, context={'request': request})
        if announcement_serializer.is_valid(raise_exception=True):
            announcement_serializer.save()
            headers = self.get_success_headers(announcement_serializer.data)
            create_notifications.send(request, announcement_serializer.data['id'])
            return Response(announcement_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(announcement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnouncementRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "pk"

    def get_serializer_class(self):
        if self.action == "partial_update":
            return AnnouncementUpdateSerializer
        else:
            return AnnouncementSerializer
