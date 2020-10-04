from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import Http404, HttpResponseRedirect
from allauth.account.views import SignupView
from main.models import Room, RoomMember
from . import forms


def raise404(request):
    raise Http404


class ModeratorSignupView(SignupView):
    form_class = forms.ModeratorSignupForm
    success_url = reverse_lazy('main-index')
    template_name = 'account/moderator_signup.html'


class UserSignupView(SignupView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('main-index')
    template_name = 'account/user_signup.html'

    def form_valid(self, form):
        self.user = form.save(self.request)
        authentication_code = form.cleaned_data['authentication_code']
        room = get_object_or_404(
            Room, authentication_code=authentication_code)
        RoomMember.objects.create(
            room=room, user=self.user, is_moderator=False)
        return HttpResponseRedirect(reverse('main-index'))
