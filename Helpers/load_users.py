import os, sys
sys.path.append('/home/naveensundar/Desktop/WallStreet18/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")

import django
django.setup()

from SellBuy.models import Share, SharePrice
import random, time
from django.contrib.auth.models import User
from SellBuy.models import (CurrentUserHolding, Share, UserHolding, UserShareQuantity)
from LoginRegister.models import UserDetail


for i in range(50):
    username = 'user'+str(i)
    password = 'abcd1234'
    name = username
    email = username + '@gmail.com'
    college = 'nitrr'
    branch = 'something'
    contact = '0123456789'

    user = User.objects.create_user(
        username=username,
        password=password
    )
    user.save()

    user_detail = UserDetail.objects.create(
        username=username,
        name=name,
        email=email,
        college=college,
        branch=branch,
        contact=contact
    )
    user_detail.save()

    user_holding = UserHolding.objects.create(
        user=user
    )
    user_holding.save()

    current_user_holding = CurrentUserHolding.objects.create(
        user=user
    )
    current_user_holding.save()

    shares = Share.objects.all()
    for share in shares:
        user_share_quantity = UserShareQuantity.objects.create(
            share=share,
            user=user,
            quantity=0
        )
        user_share_quantity.save()

    print('{} created'.format(username))