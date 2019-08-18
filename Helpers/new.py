import os, sys
# sys.path.append('/home/pratibha/Desktop/wallstreet18/')
sys.path.append('/home/shreyansh/Projects/DjangoProjects/WallStreet18/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")
import django
django.setup()

from SellBuy.models import Share, SharePrice
import random, time
from Helpers.utils import get_or_none


def generate_share_price():
    time.sleep(1)
    share_obj = get_or_none(Share, id=1)
    last_price = share_obj.current_price
    share_obj.current_price = 17364.14
    share_obj.previous_price = last_price
    share_obj.save()
    share_price_obj = SharePrice.objects.create(
            share=share_obj,
            price=last_price
    )
    share_price_obj.save()
    print("Price changed")
    return True

if __name__ == "__main__":
    generate_share_price()
