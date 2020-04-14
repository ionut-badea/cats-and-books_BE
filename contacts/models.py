from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.urls import reverse
import uuid


class Message(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    name = models.CharField(_('name'),
                            max_length=25,
                            blank=True,
                            null=True)
    email = models.CharField(_('email'),
                             max_length=50,
                             blank=False,
                             null=False)
    reply = models.BooleanField(_('reply'),
                                default=False)
    body = models.TextField(_('message'),
                            max_length=500,
                            blank=False,
                            null=False)
    terms = models.BooleanField(_('terms'),
                                default=False)
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        default_related_name = 'messages'
        ordering = ['email']
        get_latest_by = ['-created']

    def __str__(self):
        return f'{self.name}, {self.email}'

    def get_absolute_url(self):
        pass
