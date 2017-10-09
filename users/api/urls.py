from django.conf.urls import url, include
from django.contrib import admin

from users.api.views import register_user, login, update_user

urlpatterns = [
    url(r'^register/$', register_user, name='api_register_user'),
    url(r'^login/$', login, name='api_login_user'),
    url(r'^update_user/$', update_user, name='api_update_user'),
]