# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.TextField()
