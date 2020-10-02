from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('volunteer_page', views.volunteer_page, name='main-volunteer_page'),
    path('user_page', views.user_page, name='main-user_page')
]
