from django.db import models
from product.models import Product
# Create your models here.
class Inventory(models.Model):
    
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        self.product

    class Meta:
        db_table = 'product_inventory'
        managed = True
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'