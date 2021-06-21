from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    username, first_name, last_name eriditati da AbstractUser
    """
    avatar = models.ImageField(
        upload_to='images/avatars/', null=True, blank=True)
    hobby = models.CharField(max_length=50, blank=True)
    sesso = models.CharField(
        choices=[('M', 'uomo'), ('F', 'donna')], max_length=1, blank=True)
