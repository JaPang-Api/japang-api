from rest_framework import serializers
from users_address.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'users_id', 'name', 'address', 'province', 'regencie', 'district', 'postal_code', 'maps', 'long', 'lat', 'created_at', 'updated_at']
