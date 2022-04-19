from django.db import models

class Variant(models.Model):
    size = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.size)

    class Meta:
        db_table = 'product_size'
        managed = True
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'