from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from blog.extensions.utils import convert_to_persian_digits


class UserAdmin(BaseUserAdmin):

    def show_premium_days_remaining(self, obj):
        if obj.has_premium():
            days = convert_to_persian_digits(obj.premium_days_remaining())
            return f'{days} روز'
    show_premium_days_remaining.short_description = 'مدت زمان باقیمانده از اشتراک ویژه'

    class HasPremiumFilter(admin.SimpleListFilter):
        title = 'اشتراک ویژه'
        parameter_name = 'has_premium'
        def lookups(self, request, model_admin):
            return(
                (1, 'بله'),
                (0, 'خیر'),
            )

        def queryset(self, request, queryset):
            value = self.value()
            if value == '1':
                return queryset.filter(premium_date__gt=timezone.now())
            elif value == '0':
                return queryset.exclude(premium_date__gt=timezone.now())
            return queryset

    # change UserAdmin form options
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_author', 'has_premium', 'show_premium_days_remaining')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_author', HasPremiumFilter)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    # addd author and premium_date field
    row = list(BaseUserAdmin.fieldsets[2][1]['fields'])
    row.insert(2, 'is_author')
    row.insert(4, 'premium_date')
    BaseUserAdmin.fieldsets[2][1]['fields'] = tuple(row)

admin.site.register(User, UserAdmin)
