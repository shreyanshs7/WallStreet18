import os, sys, schedule, time, random
# sys.path.append('/home/pratibha/Desktop/wallstreet18/')
# sys.path.append('/home/naveensundar/Desktop/WallStreet18/')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")
# import django
# django.setup()

from .models import Share, SharePrice
# from WallStreetML.wallstreet import sharePrice

def share_price_update():
    print("ins shaere piijjib")
    share_obj = Share.objects.all()
    for share in share_obj:
        # Changing each share price
        old_share_price = share.current_price
        new_share_price = (old_share_price) * (random.uniform(0.7, 1.3))
        if new_share_price < 1000:
            new_share_price = (new_share_price)*(random.uniform(1.1, 1.3))
        elif new_share_price > random.randint(50000,60000):
            new_share_price = (new_share_price)*(random.uniform(0.7, 0.9))
        new_share_price = round(new_share_price, 2)
        new_share = SharePrice.objects.create(share=share, price=new_share_price)
        new_share.save()
        share.current_price = new_share_price
        share.previous_price = old_share_price
        share.save()

        # old_share_price = share.current_price
        # new_share_price = sharePrice(share.name, old_share_price)
        # new_share_price = round(new_share_price, 2)
        # new_share = SharePrice.objects.create(share=share, price=new_share_price)
        # new_share.save()
        # share.current_price = new_share_price
        # share.previous_price = old_share_price
        # share.save()
    print("Share price changed")
    return True

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
