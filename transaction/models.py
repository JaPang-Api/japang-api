from django.db import models

# Create your models here.

class Transaction (models.Model):
    invoice_no = models.CharField(max_length=100, blank=True)
    invoice_id = models.CharField(max_length=100, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    invoice_url = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    expiry_date = models.CharField(max_length=100, blank=True)
    delivery_address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'transaction'


    def __str__(self):
        return self.name
