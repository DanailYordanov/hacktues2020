from django.shortcuts import render


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

def room_volunteer(request):
    return render(request, 'main/room_volunteer.html')

def create_group(request):
    return render(request, 'main/create_group.html')
