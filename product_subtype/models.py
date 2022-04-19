from django.db import models

from product_type.models import Type


class SubType(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(
        Type, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'product_subtype'
        managed = True
        verbose_name = 'SubType'
        verbose_name_plural = 'SubTypes'
