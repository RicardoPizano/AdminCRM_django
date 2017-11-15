from django.conf.urls import url

from estadistic.api.views import clients_feeling


urlpatterns = [
    url(r'^clients_feeling/$', clients_feeling, name='api_clients_feeling'),
]