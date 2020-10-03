from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('volunteer_login', views.volunteer_page, name='main-volunteer_page'),
    path('user_login', views.user_page, name='main-user_page'),
    path('volunteer', views.volunteer_profile, name='main-volunteer_profile'),
    path('create_event', views.create_event, name='main-create_event'),
    path('user',views.user,name='main-user'),
    path('create_group', views.create_group, name='main-create_group'),

]
