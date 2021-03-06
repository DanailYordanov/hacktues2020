from django.db import models
from django.conf import settings


class Room(models.Model):
    name = models.CharField(max_length=30)
    authentication_code = models.CharField(max_length=5)
    moderators = models.ManyToManyField(settings.AUTH_USER_MODEL)


class RoomMember(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='room_members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_moderator = models.BooleanField()


class Event(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='room_events')
    creation_date = models.DateTimeField(auto_now_add=True)
    event = models.CharField(max_length=100)


class EventList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='list')
    content = models.TextField()
