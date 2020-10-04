from django.shortcuts import render, redirect
from .forms import CreateRoomForm
from .models import RoomMember, Room
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


def volunteer_login(request):
    return render(request, 'main/volunteer_login.html')


def user_login(request):
    return render(request, 'main/user_login.html')


def volunteer_profile(request):
    context = {
        'user': {
            'first_name': 'Калоян',
            'last_name': 'Георгиев',
            'login': 'kalooo914@gmail.com',
            'rooms': [
                {
                    'id': 1,
                    'name': 'бл. 822 ж.к. Люлин 8',
                }
            ]

        }
    }
    return render(request, 'main/volunteer_profile.html')

def create_event(request):
    return render(request, 'main/create_event.html')


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
                'author':'Калоян',
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
def room_volunteer(request):
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
                'author':'Калоян',
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
    return render(request, 'main/room_volunteer.html', context)


@login_required
def create_room(request):

    if request.method == 'POST':
        form = CreateRoomForm(request.POST)

        if form.is_valid():

            authentication_code = get_random_string(5)
            moderators = [request.user]
            instance = form.save(commit=False)
            instance.authentication_code = authentication_code
            form.save()

            RoomMember.objects.create(
                room=instance, user=request.user, is_moderator=True)

            return redirect('room')

    else:
        form = CreateRoomForm()

    context = {
        'form': form
    }

    return render(request, 'main/create_room.html', context)
