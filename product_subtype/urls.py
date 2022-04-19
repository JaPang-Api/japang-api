
from django.urls import path, include
from .views import SubTypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'master/sub-types', SubTypeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
