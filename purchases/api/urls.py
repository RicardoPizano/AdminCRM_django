from django.conf.urls import url

from purchases.api.views import register_purchase, get_product_rate, register_rate, view_my_purchases

urlpatterns = [
    url(r'^register_purchase/$', register_purchase, name='api_register_purchase'),

    url(r'^register_rate/$', register_rate, name='api_register_rate'),
    url(r'^get_product_rate/(?P<product_id>\d+)/$', get_product_rate, name='api_get_product_rate'),
    url(r'^view_my_purchases/(?P<user_id>\d+)/$', view_my_purchases, name='api_view_my_purchases'),

]