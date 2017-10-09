from django.conf.urls import url, include
from django.contrib import admin

from products.api.views import get_products_types, get_products, get_products_by_type, register_product_type, register_product, update_product_type, update_product, delete_product_type, delete_product

urlpatterns = [
    # Get products and products types
    url(r'^get_products_types/$', get_products_types, name='api_get_products_types'),
    url(r'^get_products/$', get_products, name='api_get_products'),
    url(r'^get_products_by_type/(?P<type_id>\d+)/$', get_products_by_type, name='api_get_products_by_type'),

    # Register a new product or product type
    url(r'^register_product_type/$', register_product_type, name='api_register_product_type'),
    url(r'^register_product/$', register_product, name='api_register_product'),

    # Update a product or product type
    url(r'^update_product_type/$', update_product_type, name='api_update_product_type'),
    url(r'^update_product/$', update_product, name='api_update_product'),

    # Delete a product or product type
    url(r'^delete_product_type/$', delete_product_type, name='api_delete_product_type'),
    url(r'^delete_product/$', delete_product, name='api_delete_product'),
]