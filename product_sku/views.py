from rest_framework import viewsets

from ecommerce_api.utils.renderers import CustomRender

from .models import ProductSku
from .serializers import SkuSerializer


class SkuViewSet(viewsets.ModelViewSet):

    queryset = ProductSku.objects.all()
    serializer_class = SkuSerializer

    renderer_classes = [CustomRender]
