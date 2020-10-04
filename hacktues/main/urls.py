from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('user-profile/', views.user_profile, name='main-user-profile'),
    path('create-event/<int:room_id>/',
         views.create_event, name='main-create-event'),
    path('room/<int:pk>/', views.room, name='main-room'),
    path('create-room/', views.create_room, name='main-create-room'),
    path('choice/', views.choice, name='main-choice'),
    path('create-list/<int:pk>/',
         views.create_list, name='main-create-list'),
    path('event/<int:pk>/', views.event_detail, name='main-event-detail'),
]
