# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler




def start(function):
    scheduler = BackgroundScheduler()
    print('job added')
    scheduler.add_job(function, 'interval', seconds=5)
    scheduler.start()


class SellbuyConfig(AppConfig):

    name = 'SellBuy'

    def ready(self):
        from .share_price_change import share_price_update
        print('loaded')
        start(share_price_update)
