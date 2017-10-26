# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=30)
    mail = models.CharField(max_length=80)
    register_date = models.DateField(auto_now=True)
    password = models.CharField(max_length=255)
    user_type = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
