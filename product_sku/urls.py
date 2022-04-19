
from django.urls import path, include
from .views import SkuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'master/skus', SkuViewSet)

urlpatterns = [path('', include(router.urls))]
