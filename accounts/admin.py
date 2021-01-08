from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .forms import (CustomUserChangeForm,
                    CustomUserCreationForm,
                    CustomPasswordCahngeForm)
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Data'), {
         'fields': ('first_name', 'last_name', 'bio', 'avatar')}),
        (_('Permissions'), {
         'fields': ('is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions')}),
        (_('Dates'), {'fields': ('date_joined', 'last_login')})
    )
    add_fieldsets = (
        (None, {'classes': ('wide'),
                'fields': ('username', 'password1', 'password2')
                }
         )
    )
    form = CustomUserChangeForm
    # add_form = CustomUserCreationForm
    change_password = CustomPasswordCahngeForm
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_active', 'is_staff', 'is_superuser',
                    'last_login', 'date_joined')
    list_filter = ('is_active', 'is_staff',
                   'is_superuser', 'groups')
    search_fields = ('username__icontains', 'email__icontains'
                     'first_name__icontains', 'last_name__icontains')
    filter_horizontal = ('groups', 'user_permissions')
