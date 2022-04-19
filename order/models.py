from django.db import models

# Create your models here.
class Order (models.Model):
    amount = models.CharField(max_length=100, blank=True)
    product_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table = 'transaction_detail'


    def __str__(self):
        return self.name