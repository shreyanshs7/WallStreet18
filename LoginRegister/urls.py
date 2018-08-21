from django.conf.urls import url
from .views import register, user_login, user_logout


urlpatterns = [
    url(r'^register/', register),
    url(r'^login/', user_login),
    url(r'logout/', user_logout)
]