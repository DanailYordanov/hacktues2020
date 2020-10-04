from django.db import models
from django.conf import settings


class Room(models.Model):
    authentication_code = models.CharField(max_length=5)


class RoomMember(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_moderator = models.BooleanField()
