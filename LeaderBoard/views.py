# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from SellBuy.models import CurrentUserHolding, UserShareQuantity
from django.shortcuts import render
from LoginRegister.models import UserDetail
from django.http import JsonResponse
from Helpers.utils import get_or_none
from django.contrib.auth.models import User

# Create your views here.
def leaderboard(request):
    return render(request, 'LeaderBoard/leaderboard.html')

def leaderboard_update(request):
    leaderboard = CurrentUserHolding.objects.order_by('current_holding').reverse()
    leaderboard_list = []
    for obj in leaderboard:
        total_holdings = obj.current_holding
        for user_share in UserShareQuantity.objects.filter(user=obj.user):
            share = user_share.share.current_price
            quantity = user_share.quantity
            total_holdings += round(share*quantity, 2)
        
        leaderboard_data = {
            "username" : obj.user.username,
            "holding" : round(total_holdings, 2),
            "index" : 0
        }
        
        leaderboard_list.append(leaderboard_data)

    leaderboard_list = sorted(leaderboard_list, key = lambda x: x['holding'], reverse = True)

    index = 1
    for o in leaderboard_list:
        o['index'] = index
        index += 1

    data = {
        "success" : True,
        "data" : leaderboard_list
    }    
    return JsonResponse(data, safe=False)