from django.db import models

class ProductSku(models.Model):
    code = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return str(self.code)

    class Meta:
        db_table = 'product_sku'
        managed = True
        verbose_name = 'ProductSku'
        verbose_name_plural = 'ProductSkus'