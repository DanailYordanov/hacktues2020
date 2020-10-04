from django.contrib import admin
from .models import Room, RoomMember, Event, EventList

admin.site.register(Room)
admin.site.register(RoomMember)
admin.site.register(Event)
admin.site.register(EventList)
