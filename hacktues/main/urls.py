from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('volunteer_login', views.volunteer_page, name='main-volunteer_page'),
    path('user_login', views.user_page, name='main-user_page'),
    path('volunteer', views.volunteer_profile, name='main-volunteer_profile'),
    path('volunteer/create_event', views.create_event, name='main-volunteer_profile/create_event'),
]
