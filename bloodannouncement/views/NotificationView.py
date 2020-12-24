from rest_framework.generics import ListCreateAPIView, ListAPIView
from ..serializers.NotificationSerializer import NotificationSerializer
from ..models.notification import Notification


class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()