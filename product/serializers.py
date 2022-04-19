from rest_framework import serializers

from .models import Product
from product_subtype.models import SubType
from product_variant.serializers import VariantSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class VariantListSerializer(serializers.ModelSerializer):

    size = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_size(self, obj):
        serializer = VariantSerializer(obj.size)
        size = serializer.data
        return size


class ProductDetailSerializer(serializers.ModelSerializer):

    variants = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SubType
        fields = '__all__'

    def get_variants(self, obj):
        queryset = Product.objects.all().filter(subtype=obj.pk)

        if queryset.count() > 0:
            serializer = VariantListSerializer(queryset, many=True)
            return serializer.data
        return None
