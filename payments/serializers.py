from rest_framework import serializers
from payments.models import Payments

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['id', 'users_id', 'transactions_id', 'invoice_id', 'invoice_url', 'expiry_date', 'status', 'amount', 'updated_at']
