from django.db import models

from product_category.models import Category
from product_type.models import Type
from product_subtype.models import SubType
from product_variant.models import Variant


class Product(models.Model):
    category = models.ForeignKey(
        Category, null=False, blank=False, on_delete=models.CASCADE)
    type = models.ForeignKey(
        Type, null=False, blank=False, on_delete=models.CASCADE)
    subtype = models.ForeignKey(
        SubType, null=False, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey(
        Variant, blank=False, null=False, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    tags = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
