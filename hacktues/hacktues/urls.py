from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from users import views as users_views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/signup/', users_views.raise404, name='account_signup'),
    path('accounts/signup/moderator/',
         users_views.ModeratorSignupView.as_view(), name='account_moderator_signup'),
    path('accounts/signup/user/',
         users_views.UserSignupView.as_view(), name='account_user_signup'),
    path('accounts/', include('allauth.urls'))
]
