from django.contrib import admin
from .models import Room, RoomMember, Event

admin.site.register(Room)
admin.site.register(RoomMember)
admin.site.register(Event)