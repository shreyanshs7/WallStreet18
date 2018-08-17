from django.conf.urls import url
from .views import register, user_login


urlpatterns = [
    url(r'^register/', register),
    url(r'^login/', user_login)
]