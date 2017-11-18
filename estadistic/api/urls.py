from django.conf.urls import url

from estadistic.api.views import clients_feeling, clients_quantity, products_quantity


urlpatterns = [
    url(r'^clients_feeling/$', clients_feeling, name='api_clients_feeling'),
    url(r'^clients_quantity/$', clients_quantity, name='api_clients_quantity'),
    url(r'^products_quantity/$', products_quantity, name='api_products_quantity'),
]
