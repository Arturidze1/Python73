from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from account.managers import UserManager
from core.models import DateTimeMixin


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixin):
    username = models.CharField(max_length=64, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=64, unique=True)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        ordering = ['-id', '-created_at']
        db_table = 'Users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

