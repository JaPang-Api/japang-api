
from django.urls import path, include
from .views import UomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'master/uom', UomViewSet)

urlpatterns = [path('', include(router.urls))]