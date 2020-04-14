from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name', 'body')}),
    )

    list_display = ('email', 'name', 'body', 'reply', 'terms', 'created')
    list_filter = ('reply', 'terms', 'created')
    search_fields = ('email__icontains', 'name__icontains', 'body__icontains')
