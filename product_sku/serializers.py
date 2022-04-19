from rest_framework import serializers

from .models import ProductSku


class SkuSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSku
        fields = '__all__'
