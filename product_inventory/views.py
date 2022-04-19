from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer

from ecommerce_api.utils.renderers import CustomRender
# Create your views here.

class InventoryViewSet(viewsets.ModelViewSet):

    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
    renderer_classes = [CustomRender]
    