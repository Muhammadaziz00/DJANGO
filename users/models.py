from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import GeekUserManeger
from django.utils import timezone

class GeekUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Адрес email", unique=True)
    is_active = models.BooleanField(verbose_name="Актив", default=True)
    is_staff = models.BooleanField(verbose_name="модератор", default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    age = models.SmallIntegerField(verbose_name="возраст", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] #можно написать обязательные поля

    objacts = GeekUserManeger()


    def __str__(self):
        return self.email
    
    class Meta:
        verbosa_name = "Гик"
        verbosa_name_plural = "Гики" 


