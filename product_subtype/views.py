from rest_framework import viewsets

from ecommerce_api.utils.renderers import CustomRender

from .models import SubType
from .serializers import SubTypeSerializer


class SubTypeViewSet(viewsets.ModelViewSet):

    queryset = SubType.objects.all()
    serializer_class = SubTypeSerializer

    renderer_classes = [CustomRender]
    
