from rest_framework import generics, response
from ecommerce_api.utils.renderers import CustomRender

from .models import CartItem
from .serializers import CartItemSerializer, ReadCartItemSerializer

import jwt


class AddToCart(generics.CreateAPIView):

    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    renderer_classes = (CustomRender,)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.current_user())
        return queryset

    def current_user(self):
        token = self.request.COOKIES.get('authorizationToken')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['id']

    def create(self, request):
        user = self.current_user()

        data = request.data

        item_instance = []

        if isinstance(data, list):

            for dt in request.data:
                dt['user'] = user
                item_instance = self.queryset.filter(
                    user=user).filter(product=dt.get('product'))
                item_instance.delete()
        else:
            data['user'] = user
            item_instance = self.queryset.filter(
                user=user).filter(product=data.get('product'))
            item_instance.delete()

        serializer = self.get_serializer(
            data=data, many=isinstance(data, list))
        if serializer.is_valid():
            serializer.save()

            return response.Response(serializer.data)
        return response.Response(serializer.errors, 400)


class CartItemList(generics.ListAPIView):
    serializer_class = ReadCartItemSerializer
    queryset = CartItem.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.current_user())
        return queryset

    def current_user(self):
        token = self.request.COOKIES.get('authorizationToken')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['id']
    
    def get(self, request, *args, **kwargs):
        print(self.serializer_class.validated_data)
        return super().get(request, *args, **kwargs)
        
