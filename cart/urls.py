from django.urls import path

from .views import AddToCart, CartItemList

urlpatterns = [
    path('order/checkout/', CartItemList.as_view(), name="cart-list"),
    path('order/add-to-cart/', AddToCart.as_view(), name="add-to-cart"),
]
