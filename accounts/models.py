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
    first_name = models.CharField(_('first name'),
                                  max_length=25,
                                  blank=True)
    last_name = models.CharField(_('last name'),
                                 max_length=25,
                                 blank=True)
    name = models.CharField(_('full name'),
                            max_length=50,
                            blank=True,
                            editable=False)
    bio = models.TextField(_('bio'),
                           blank=True)
    avatar = models.ImageField(_('avatar'),
                               upload_to='images/users',
                               blank=True)

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.name = f'{self.first_name} {self.last_name}'
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        default_related_name = 'users'
        ordering = ['username']
        get_latest_by = ['-date_joined']
