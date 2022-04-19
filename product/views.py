import json
import jwt

from rest_framework import generics, viewsets
from product_subtype.models import SubType
from product_variant.models import Variant
from ecommerce_api.utils.renderers import CustomRender
from rest_framework.response import Response
from .models import Product
from product_category.models import Category
from .serializers import ProductSerializer, ProductDetailSerializer
from product_category.serializers import CategorySerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from product_subtype.views import SubTypeViewSet
from rest_framework.decorators import action
from cart.models import CartItem
from cart.serializers import CartItemSerializer


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    lookup_field = 'id'

    renderer_classes = (CustomRender,)


class ProductDetailWithCartItem(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = SubType.objects.all()

    lookup_field = 'id'

    def current_user(self):
        token = self.request.COOKIES.get('authorizationToken')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['id']

    def get_serializer_context(self):

        context = super().get_serializer_context()
        context["user_id"] = self.current_user()

        return context

    def get_cart_items(self):
        queryset = CartItem.objects.all().filter(user=self.current_user())
        if queryset.count() > 0:
            serializer = CartItemSerializer(queryset, many=True)
            return serializer.data
        return None

    def transaction_arr(self):

        transactions = None
        variants_data = self.get_cart_items()
        total_price = 0

        if variants_data:

            if isinstance(variants_data, list):

                for variant in variants_data:
                    temp_price = variant['price'] * variant['amount']
                    total_price += temp_price

            transactions = [{
                "total_price": total_price,
                "variants": variants_data
            }]

        return transactions

    def get(self, request, *args, **kwargs):

        ser = ProductDetailSerializer(self.get_object())
        data = ser.data
        data['cart_items'] = {
            'transactions': self.transaction_arr()
        }

        return Response(data)


class ProductCategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    renderer_classes = (CustomRender,)


class ProductByCategoryList(APIView):

    renderer_classes = (CustomRender,)

    def get_object(self, category):
        try:
            return Product.objects.filter(category=category)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category):
        products = self.get_object(category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
