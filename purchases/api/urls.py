from django.conf.urls import url

from purchases.api.views import register_purchase

urlpatterns = [
    url(r'^register_purchase/$', register_purchase, name='api_register_purchase'),
]