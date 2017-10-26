from django.conf.urls import url, include
from django.contrib import admin

from users.api.views import register_user, login, update_user, delete_user, view_profile, get_users_by_type

urlpatterns = [
    url(r'^register/$', register_user, name='api_register_user'),
    url(r'^login/$', login, name='api_login_user'),
    url(r'^update_user/$', update_user, name='api_update_user'),
    url(r'^delete_user/$', delete_user, name='api_delete_user'),
    url(r'^view_profile/$', view_profile, name='api_view_profile'),
    url(r'^get_users_by_type/$', get_users_by_type, name='api_get_users_by_type'),
]