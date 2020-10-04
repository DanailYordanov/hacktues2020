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
    return render(request, 'main/volunteer_profile.html')


def create_event(request):
    return render(request, 'main/create_event.html')


def room_user(request):
    return render(request, 'main/room_user.html')

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
                'author': 'Калоян',
                'content': 'Това е първото събитие',
                'id': 1,
            },
            {
                'title': 'Събитие второ',
                'author': 'Дани',
                'content': 'Това е второто събитие',
                'id': 2,
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
