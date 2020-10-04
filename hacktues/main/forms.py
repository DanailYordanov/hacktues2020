from django import forms
from .models import Room, Event


class CreateRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', ]


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event', ]
