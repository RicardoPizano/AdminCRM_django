# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from products.models import ProductType, Product

# Register your models here.
admin.site.register(ProductType)
admin.site.register(Product)