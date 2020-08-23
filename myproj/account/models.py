from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name='نویسنده')
    premium_date = models.DateTimeField(default=timezone.now, verbose_name='پایان اشتراک')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username
    