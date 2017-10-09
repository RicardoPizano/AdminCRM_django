from django.conf.urls import url, include
from django.contrib import admin

from products.api.views import get_products_types, get_products, get_products_by_type

urlpatterns = [
    url(r'^get_products_types/$', get_products_types, name='api_get_products_types'),
]