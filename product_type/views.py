from rest_framework import viewsets

from ecommerce_api.utils.renderers import CustomRender

from .models import Type
from .serializers import TypeSerializer


class TypeViewSet(viewsets.ModelViewSet):

    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    renderer_classes = [CustomRender]
