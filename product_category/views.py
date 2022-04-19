from rest_framework import viewsets

from ecommerce_api.utils.renderers import CustomRender

from .models import Category
from .serializers import CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    renderer_classes = [CustomRender]
