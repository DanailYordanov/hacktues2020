from django.shortcuts import render

def register(request):
    return render(request, 'account/signup.html')
def login(request):
    return render(request, 'account/login.html')
def password_reset(request):
    return render(request, 'account/password_reset.html')