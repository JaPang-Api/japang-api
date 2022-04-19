from __future__ import unicode_literals
from django.contrib import admin

from users_address.models import Address

# Register your models here.

class AddressAdmin (admin.ModelAdmin):
    list_display = ['users_id', 'name', 'address', 'province', 'regencie', 'district', 'postal_code', 'maps', 'long', 'lat', 'created_at', 'updated_at']
    search_fields = ['users_id', 'name', 'address']

admin.site.register(Address, AddressAdmin)
