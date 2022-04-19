from django.urls import path
from .views import GetInvoice, Payments, Invoice

urlpatterns = [
    path('payement', Payments.as_view()),
    path('invoice', Invoice.as_view()),
    path('get_invoice', GetInvoice.as_view()),
]
