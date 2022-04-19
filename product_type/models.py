from django.db import models

from product_category.models import Category


class Type(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    category = models.ForeignKey(
        Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_type'
        managed = True
        verbose_name = 'Type'
        verbose_name_plural = 'Types'
