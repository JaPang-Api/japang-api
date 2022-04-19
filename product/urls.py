from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductByCategoryList, ProductCategoryList, ProductViewSet, ProductDetailWithCartItem

router = DefaultRouter()
router.register(r'master/product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/<int:id>/', ProductDetailWithCartItem.as_view(), name="product-categories-list"),
    path('product/categories/', ProductCategoryList.as_view(), name="product-categories-list"),
    path('product/category/<str:category>/', ProductByCategoryList.as_view(), name="product-list-by-categories"),
]
