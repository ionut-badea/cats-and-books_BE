from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
import uuid


class User(AbstractUser):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    email = models.CharField(_('email'),
                             max_length=50,
                             unique=True)
    bio = models.TextField(_('bio'),
                           max_length=200,
                           blank=True,
                           null=True)
    avatar = models.ImageField(_('avatar'),
                               upload_to='images/users',
                               blank=True,
                               null=True)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        default_related_name = 'users'
        ordering = ['username']
        get_latest_by = ['-date_joined']

    def get_absolute_url(self):
        pass
