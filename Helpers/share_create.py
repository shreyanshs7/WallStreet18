import os, sys
sys.path.append('/home/shreyansh/Projects/DjangoProjects/WallStreet18/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")
import django
django.setup()

from SellBuy.models import Share, SharePrice
import random, time

shares = ['Star Labs','Lannister Corp','Stark Industries','Pied Piper', 'Warner Bros.', 'Marvel Studios']

def generate_share_price():
    time.sleep(1)
    for share in shares:
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
    time.sleep(2)       
    return True   

if __name__ == "__main__":
    generate_share_price()