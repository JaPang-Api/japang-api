from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Payments (models.Model):
    users_id = models.IntegerField(blank=True, null=True)
    transactions_id = models.IntegerField(blank=True, null=True)
    
    invoice_id = models.CharField(max_length=100, blank=True)
    invoice_url = models.CharField(max_length=100, blank=True)
    expiry_date = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=100, blank=True)

    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users_payments'


    def __str__(self):
        return self.name
