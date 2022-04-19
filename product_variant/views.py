from rest_framework import viewsets

from ecommerce_api.utils.renderers import CustomRender

from .models import Variant
from .serializers import VariantSerializer


class VariantViewSet(viewsets.ModelViewSet):

    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

    renderer_classes = [CustomRender]
