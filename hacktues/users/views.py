from django.shortcuts import render
from allauth.account.views import SignupView
from django.urls import reverse_lazy
from django.http import Http404
from . import forms


def raise404(request):
    raise Http404


class ModeratorSignupView(SignupView):
    # form_class = forms.ModeratorSignupForm
    # success_url = reverse_lazy('main-index')
    pass


class UserSignupView(SignupView):
    pass
