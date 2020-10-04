from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from users import views as users_views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'))
]
