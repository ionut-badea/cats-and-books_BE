from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name', 'status', 'terms')}),
    )

    list_display = ('email', 'name', 'status', 'terms', 'created', 'updated')
    list_filter = ('status', 'terms', 'created')
    search_fields = ('email__icontains', 'name__icontains')
