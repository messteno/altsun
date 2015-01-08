from django.contrib import admin
from contact.models import Contact
from django.db import models


class ContactAdmin(admin.ModelAdmin):
    list_display_links = ('id', )
    list_display = ('id', 'email', )
    search_fields = ('email', )
    list_editable = ()
admin.site.register(Contact, ContactAdmin)
