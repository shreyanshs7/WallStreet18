from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .share_price_change import share_price_update

def prh():
    print("hello world")

def start():
    scheduler = BackgroundScheduler()
    print('job added')
    scheduler.add_job(prh, 'interval', seconds=5)
    scheduler.start()