from rest_framework import viewsets

from ecommerce_api.utils.renderers import CustomRender

from .models import Uom
from .serializers import UomSerializer


class UomViewSet(viewsets.ModelViewSet):

    queryset = Uom.objects.all()
    serializer_class = UomSerializer

    renderer_classes = [CustomRender]
