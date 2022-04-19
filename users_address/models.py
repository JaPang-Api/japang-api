from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Address (models.Model):
    name = models.CharField(max_length=100)
    users_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True)
    province = models.CharField(max_length=100, blank=True)
    regencie = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    maps = models.CharField(max_length=100, blank=True)
    long = models.CharField(max_length=100, blank=True)
    lat = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users_address'


    def __str__(self):
        return self.name
