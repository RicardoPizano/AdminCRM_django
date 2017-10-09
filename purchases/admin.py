# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from purchases.models import Purchases, Rate

# Register your models here.
admin.site.register(Purchases)
admin.site.register(Rate)