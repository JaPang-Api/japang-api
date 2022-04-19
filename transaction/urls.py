from django.urls import path
from .views import Transaction, Callback

urlpatterns = [
    path('transaction', Transaction.as_view()),
    path('callback', Callback.as_view()),
]
