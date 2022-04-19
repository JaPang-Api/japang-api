from django.db import models

class Uom(models.Model):
    code = models.CharField(max_length=5, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'unit_of_measure'
        managed = True
        verbose_name = 'Uom'
        verbose_name_plural = 'Uoms'