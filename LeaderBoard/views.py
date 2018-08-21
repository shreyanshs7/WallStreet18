# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from SellBuy.models import CurrentUserHolding
from django.shortcuts import render
from LoginRegister.models import UserDetail
from django.http import JsonResponse

# Create your views here.
def leaderboard(request):
    return render(request, 'LeaderBoard/leaderboard.html')

def leaderboard_update(request):
    leaderboard = CurrentUserHolding.objects.order_by('current_holding').reverse()
    leaderboard_list = []
    for obj in leaderboard:
        user_object = UserDetail.objects.get(username=obj.user.username)
        leaderboard_data = {
            "name" : user_object.name,
            "username" : user_object.username,
            "holding" : round(obj.current_holding, 3)
        }
        leaderboard_list.append(leaderboard_data)

    data = {
        "success" : True,
        "data" : leaderboard_list
    }    
    return JsonResponse(data, safe=False)