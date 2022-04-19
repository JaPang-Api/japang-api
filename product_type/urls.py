
from django.urls import path, include
from .views import TypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'master/types', TypeViewSet)

urlpatterns = [path('', include(router.urls))]