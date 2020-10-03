from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def volunteer_page(request):
    return render(request, 'main/volunteer_page.html')

def user_page(request):
    return render(request, 'main/user_page.html')

def volunteer_profile(request):
    return render(request, 'main/volunteer_profile.html')

def create_event(request):
    return render(request, 'main/create_event.html')

def user(request):
    return render(request, 'main/user.html')