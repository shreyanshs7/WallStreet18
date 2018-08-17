# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from SellBuy.models import CurrentUserHolding
from django.shortcuts import render
from LoginRegister.models import UserDetail
from django.http import JsonResponse

# Create your views here.
def leaderboard(request):
    leaderboard = CurrentUserHolding.objects.order_by('current_holding').reverse()
    return render(request,'LeaderBoard/leaderboard.html', {'leaderboard' : leaderboard})

def leaderboard_update(request):
    leaderboard = CurrentUserHolding.objects.order_by('current_holding').reverse()
    for obj in leaderboard:
        user_object = UserDetail.objects.get(username=obj.username)
        leaderboard_date = {
            "name" : user_object.name,
            "username" : user_object.username,
            "holding" : obj.current_holding
        }

    data = {
        "success" : True,
        "data" : leaderboard_date
    }    
    return JsonResponse(data, safe=False)