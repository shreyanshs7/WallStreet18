from django.conf.urls import url
from django.contrib.auth.views import login
from .views import dashboard, current_money, transaction, dashboard_data, share_graph

urlpatterns = [
    url(r'^dashboard/', dashboard),
    url(r'^data/', dashboard_data),
    url(r'^money/', current_money),
    url(r'^transaction/', transaction),
    url(r'^graph/(\d+)', share_graph)
]