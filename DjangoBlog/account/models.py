from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name='نویسنده', help_text='نشان میدهد که آیا این کاربر میتواند مطلب ارسال کند یا خیر.')
    premium_date = models.DateTimeField(default=timezone.now, verbose_name='پایان اشتراک')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username

    def premium_days_remaining(self):
        return (self.premium_date - timezone.now()).days
    premium_days_remaining.short_description = 'مدت زمان باقیمانده از اشتراک ویژه'

    def has_premium(self):
        return self.premium_date > timezone.now()
    has_premium.boolean = True
    has_premium.short_description = 'اشتراک ویژه'