
from django.urls import path, include
from .views import CategoriesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'master/categories', CategoriesViewSet)

urlpatterns = [path('', include(router.urls))]
