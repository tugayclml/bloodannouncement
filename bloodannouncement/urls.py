from django.urls import path
from .views.UserView import UserListCreateView, ChangeUserPasswordView, UserRetrieveUpdateViewSet
from .views.AnnouncementView import AnnouncementListCreateView, AnnouncementRetrieveUpdateView
from .views.NotificationView import NotificationListView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-create'),
    path("users/changepassword/", ChangeUserPasswordView.as_view(), name="change-password"),
    path('login/', obtain_auth_token, name="login"),
    path("users/<int:pk>/", UserRetrieveUpdateViewSet.as_view({"get": "retrieve", "patch": "partial_update"})),
    path('announcement/', AnnouncementListCreateView.as_view(), name='announcement-create'),
    path('announcement/<int:pk>/', AnnouncementRetrieveUpdateView.as_view({"get": "retrieve", "patch": "partial_update"}), name='announcement-update-retrieve'),
    path('notifications/', NotificationListView.as_view(), name="notifications"),
]
