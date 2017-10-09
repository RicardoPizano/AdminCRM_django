from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^users/', include('users.api.urls')),
    url(r'^products/', include('products.api.urls')),
    url(r'^purchases/', include('purchases.api.urls')),
]