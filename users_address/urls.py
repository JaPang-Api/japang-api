from django.urls import path
from .views import AddressView

urlpatterns = [
    path('user_address', AddressView.as_view()),
]
