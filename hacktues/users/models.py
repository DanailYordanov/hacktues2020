from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(verbose_name="Снимка", default='default.png',
                              upload_to='profile_pics', blank=True, null=False)
    email = models.EmailField(null=True)
