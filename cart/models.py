from django.db import models

from product.models import Variant, Product
from users.models import User

# Create your models here.
class CartItem(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cart_item'
        managed = True
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'
    
    def __str__(self):
        return str(self.id)