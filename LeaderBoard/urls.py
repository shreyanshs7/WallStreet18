from django.conf.urls import url
from django.contrib.auth.views import login
from .views import leaderboard, leaderboard_update

urlpatterns = [
    url(r'^thisisasecret9787/', leaderboard),
    url(r'^update/', leaderboard_update)
]