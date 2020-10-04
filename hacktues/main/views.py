from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateRoomForm, CreateEventForm
from .models import RoomMember, Room
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def index(request):
    return render(request, 'main/index.html')


def user_profile(request):

    room_members = RoomMember.objects.filter(user=request.user)
    rooms = []

    for room_member in room_members:
        rooms.append(room_member.room)

    context = {
        'rooms': rooms
    }

    return render(request, 'main/user_profile.html', context)


def create_event(request, room_id):

    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = CreateEventForm(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.room = room
            form.save()

            return redirect('main-room', pk=room.id)

    else:
        form = CreateEventForm()

    context = {
        'form': form,
        'room_id': room_id
    }

    return render(request, 'main/create_event.html', context)


def room(request, pk):
    room = get_object_or_404(Room, id=pk)

    users = []
    for room_member in room.room_members.all():
        users.append(room_member.user)

    if request.user in users:
        context = {
            'room': room
        }
        return render(request, 'main/room.html', context)
    else:
        raise PermissionDenied


def room_user(request):
    context = {
        'users': [
            'Пенка Георгиева',
            'Радка Тодорова',
            'Васил Тодоров',
            'Илияна Вълева'
        ],
        'events': [
            {
                'title': 'ПЪРВО СЪБИТИЕ!',
                'author': 'Калоян',
                'content': 'Ще посещавам Kaufland в квартала на 6 октомври около 12 часа. Ако имате заявки пратете списък!',
                'id': 1,
                'date_posted': '4 Октомври 2020 17:39'
            },
            {
                'title': 'Събитие второ',
                'author': 'Дани',
                'content': 'Това е второто събитие',
                'id': 2,
                'date_posted': '2 Октомври 2020 14:56'
            }
        ]
    }
    return render(request, 'main/room_user.html', context)


def choice(request):
    return render(request, 'main/choice.html')


@login_required
def create_room(request):

    if request.method == 'POST':
        form = CreateRoomForm(request.POST)

        if form.is_valid():

            authentication_code = get_random_string(5)
            instance = form.save(commit=False)
            instance.authentication_code = authentication_code
            form.save()

            RoomMember.objects.create(
                room=instance, user=request.user, is_moderator=True)

            return redirect('main-room', pk=instance.id)

    else:
        form = CreateRoomForm()

    context = {
        'form': form
    }

    return render(request, 'main/create_room.html', context)
