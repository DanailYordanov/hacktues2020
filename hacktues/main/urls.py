from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('volunteer_login/', views.volunteer_login, name='main-volunteer_login'),
    path('user_login/', views.user_login, name='main-user_login'),
    path('volunteer/', views.volunteer_profile, name='main-volunteer_profile'),
    path('create_event/', views.create_event, name='main-create_event'),
    path('room_user/', views.room_user, name='main-room_user'),
    path('room_user/new_list', views.create_list, name='main-new_list'),
    path('room_volunteer/', views.room_volunteer, name='main-room_volunteer'),
    path('create_room/', views.create_room, name='main-create-room'),
    path('choice/', views.choice, name='main-choice'),
    path('room_volunteer/event', views.event_detail, name='main-event_detail')

]
