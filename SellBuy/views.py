# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Helpers.utils import assert_found, get_or_none, assert_not_found

from .models import CurrentUserHolding, Share, SharePrice, UserShareQuantity


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated():
        shares = Share.objects.all()
        return render(request, 'SellBuy/dashboard.html', { 'shares' : shares })
    else:
        return HttpResponseRedirect('/auth/login/')
def dashboard_data(request):
    user = request.user
    user_share_quantity = UserShareQuantity.objects.filter(user=user)
    data = []
    for obj in user_share_quantity:
        current_price = obj.share.current_price
        previous_price = obj.share.previous_price

        percentage_share_change = round((previous_price / current_price), 2)
        temp_data = {}
        temp_data['share'] = obj.share.name
        temp_data['current_price'] = obj.share.current_price
        temp_data['previous_price'] = obj.share.previous_price
        temp_data['percentage_share_change'] = percentage_share_change
        temp_data['quantity'] = obj.quantity

        if current_price >= previous_price:
            temp_data['share_change'] = "increase"
        else:
            temp_data['share_change'] = "decrease"
        data.append(temp_data)

    response = {}
    response['success'] = True
    response['data'] = data

    return JsonResponse(response,safe=False)

@csrf_exempt
def current_money(request):
    username = request.user.username
    user_obj = get_or_none(User, username=username)
    response = assert_not_found(user_obj, "User not found")
    if not response['success']:
        return JsonResponse(response, safe=False)
    current_user_holding_object = get_or_none(CurrentUserHolding, user=user_obj)
    response = assert_not_found(current_user_holding_object, "User holding not found")
    if not response['success']:
        return JsonResponse(response, safe=False)
    money = current_user_holding_object.current_holding
    response = {
        "success": True,
        "message": "Your current money is %s" % (str(money)),
        "money": round(money,3)
    }
    return JsonResponse(response, safe=False)

@csrf_exempt
def transaction(request):
    if request.method == "POST":
        share_id = request.POST.get('dropdown')
        quantity = int(request.POST.get('quantity'))
        button = request.POST.get('button')
        username = request.user.username
        user = User.objects.get(username=username)
        current_user_holding = get_or_none(CurrentUserHolding, user=user)
        response = assert_not_found(current_user_holding, "User holding not found")
        if not response['success']:
            return JsonResponse(response, safe=False)
        current_money = current_user_holding.current_holding
        share_obj = get_or_none(Share, id=share_id)
        response = assert_not_found(share_obj, "Share not found")
        if not response['success']:
            return JsonResponse(response, safe=False)
        share_price = share_obj.current_price
        share_name = share_obj.name

        try:
            user_share_quantity = UserShareQuantity.objects.get(user=user, share=share_obj)
        except Exception as e:
            print(str(e))
            JsonResponse({"error": "Some error occured"}, safe=False)
        previous_quantity = user_share_quantity.quantity

        response = {}
        if quantity > int(0):
            if button == "BUY":
                if (share_price) * (quantity) <= current_money:
                    user_share_quantity.quantity = previous_quantity + quantity
                    user_share_quantity.save()

                    current_user_holding.current_holding = (current_money) - (share_price * quantity)
                    current_user_holding.save()

                    response['success'] = True
                    response['message'] = ("Bought %s shares of %s")%(str(quantity), share_name)
                    return JsonResponse(response, safe=False)
                response['success'] = False
                response['message'] = ("Money is less only %s share can be bought") % (str(int(current_money / share_price)))
                return JsonResponse(response, safe=False)
            if button == "SELL":
                if previous_quantity == int(0):
                    response['success'] = False
                    response['message'] = ("You haven't bought shares of %s") % (share_name)
                    return JsonResponse(response, safe=False)
                elif previous_quantity >= quantity:
                    user_share_quantity.quantity = previous_quantity - quantity
                    user_share_quantity.save()

                    current_user_holding.current_holding = (current_money) + (share_price * quantity)
                    current_user_holding.save()

                    response['success'] = True
                    response['message'] = ("Sold %s share of %s") % (str(quantity), share_name)
                    return JsonResponse(response, safe=False)
                response['success'] = False
                response['message'] = ("You have only %s share of %s to sell") % (str(previous_quantity), share_name)
                return JsonResponse(response, safe=False)
        else:
            response['success'] = False
            response['message'] = "Be smart and enter a valid quantity"
            return JsonResponse(response, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, safe=False)

@csrf_exempt
def share_graph(request):
    share_id = request.POST.get('id')
    share = get_or_none(Share, id=share_id)
    response = assert_not_found(share, "Share not found")
    if not response['success']:
        return JsonResponse(response, safe=False)
    share_price = SharePrice.objects.filter(share=share)
    x = []
    y = []
    for obj in share_price:
        time = obj.time
        time = time.strftime("%H:%M")
        x.append(time)
        y.append(obj.price)
    data = {
        "success" : True,
        "share_price" : y,
        "share_time" : x
    }
    return JsonResponse(data, safe=False)    
        