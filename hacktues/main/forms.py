from django import forms
from .models import Room, Event, EventList


class CreateRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', ]


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event', ]


class CreateEventListForm(forms.ModelForm):

    class Meta:
        model = EventList
        fields = ['content', ]
