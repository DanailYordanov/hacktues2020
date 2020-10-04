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

def create_group(request):
    return render(request, 'main/create_group.html')
