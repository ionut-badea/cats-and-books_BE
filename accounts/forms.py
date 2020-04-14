from .models import User
from django import forms
from django.contrib.auth.forms import (UserChangeForm,
                                       UserCreationForm,
                                       PasswordChangeForm)


class CustomPasswordCahngeForm(PasswordChangeForm):
    class Meta:
        model = User
        field = ('password1', 'password2')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
