from django.shortcuts import render, redirect


def index(request):
    if request.method == "POST":
        return redirect('main-user_login')
    return render(request, 'main/index.html')

def volunteer_login(request):
    return render(request, 'main/volunteer_login.html')

def user_login(request):
    return render(request, 'main/user_login.html')

def volunteer_profile(request):
    return render(request, 'main/volunteer_profile.html', context)

def create_event(request):
    return render(request, 'main/create_event.html')

def room_user(request):
    return render(request, 'main/room_user.html')

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

def create_group(request):
    return render(request, 'main/create_group.html')
