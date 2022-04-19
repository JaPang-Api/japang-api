import json
from rest_framework import serializers

from .models import CartItem
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError


class CartItemSerializer(serializers.ModelSerializer):

    price = serializers.SerializerMethodField()
    # product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'amount', 'product', 'user', 'price']
        read_only_fields = ['price'] 

    def get_price(self, obj):
        queryset = Product.objects.get(id=obj.product.id)
        serialize = ProductSerializer(queryset)
        data = serialize.data
        return data['price']

class ReadCartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'amount', 'product', 'user']
