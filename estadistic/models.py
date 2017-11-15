# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Statistic(models.Model):
    clients_totals = models.IntegerField()
    purchases_totals = models.IntegerField()
    register_date = models.DateField(auto_now_add=True)
