from django.contrib import admin
from django.urls import path, include
from users import views as auth_views
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login, name= 'login'),
    path('password_reset', auth_views.password_reset, name='password_reset'),
]
