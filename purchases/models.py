# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User
from products.models import Product


# Create your models here.
class Purchases(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_purchase = models.DateField(auto_now_add=True)


class Rate(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    score = models.IntegerField()
    comment = models.TextField(blank=True)
