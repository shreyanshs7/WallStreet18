import os, sys
# sys.path.append('/home/pratibha/Desktop/wallstreet18/')
sys.path.append('/home/naveensundar/Desktop/WallStreet18/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")
import django
django.setup()

from SellBuy.models import Share, SharePrice
import random, time

shares = ['Oscorp','Wayne Enterprises','Stark Industries','Pied Piper', 'Warner Bros.', 'Marvel Studios']

def generate_share_price():
    time.sleep(1)
    for share in shares:
        print(share)
        price = round(random.uniform(1360,7423),2)
        share_obj = Share.objects.create(
            name=share,
            current_price=price,
            previous_price=price
        )
        share_obj.save()
        share_price_obj = SharePrice.objects.create(
            share=share_obj,
            price=price
        )
        share_price_obj.save()
    return True

if __name__ == "__main__":
    generate_share_price()
