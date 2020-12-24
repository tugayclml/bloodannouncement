from django.contrib import admin
from .models.user import User
from .models.announcement import Announcement

admin.site.register(User)
admin.site.register(Announcement)