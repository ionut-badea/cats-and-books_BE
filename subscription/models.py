from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import uuid


class Subscriber(models.Model):
    uid = models.UUIDField(_('id'),
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    name = models.CharField(_('name'),
                            max_length=25,
                            blank=True)
    email = models.CharField(_('email'),
                             max_length=50,
                             unique=True)
    terms = models.BooleanField(_('terms and conditions'),
                                default=False)
    status = models.BooleanField(_('subscribed'),
                                 default=True)
    created = models.DateTimeField(_('created'),
                                   auto_now_add=timezone.now)
    updated = models.DateTimeField(_('updated'),
                                   auto_now=timezone.now)

    objects = models.Manager()

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')
        default_related_name = 'subscribers'
        ordering = ['-updated']
        get_latest_by = ['-created']

    def __str__(self):
        return f'{self.name}, {self.email}'
