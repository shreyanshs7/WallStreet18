# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Helpers.utils import assert_found, get_or_none
from SellBuy.models import (CurrentUserHolding, Share, UserHolding,
                            UserShareQuantity)

from .models import UserDetail

# Create your views here.

def register_get(request):
    response = {}
    response['type'] = 'register_get'
    return response

def register_post(request):
    username = request.POST.get('username')
    user = get_or_none(User, username=username)
    response = assert_found(user,"User with this username already exists")
    if not response['success']:
        return response
    password = request.POST.get('password')
    name = request.POST.get('name')
    email = request.POST.get('email')
    college = request.POST.get('college')
    branch = request.POST.get('branch')
    contact = request.POST.get('contact')

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
    user_share_quantity_list = []
    for share in shares:
        user_share_quantity = UserShareQuantity(
            share=share,
            user=user,
            quantity=0
        )
        user_share_quantity_list.append(user_share_quantity)
    UserShareQuantity.objects.bulk_create(user_share_quantity_list)

    response = {
        'success' : True,
        'message' : "User registered",
        'type' : 'register_post',
        "user" : {
            "id" : user.id,
            "username" : user.username
        }
    }

    return response

register_request_methods = {
    "POST" : register_post,
    "GET" : register_get
}

@csrf_exempt
def register(request):
    function = register_request_methods[request.method]
    response = function(request)
    if request.method == 'GET':
        return render(request, 'LoginRegister/register.html')
    if request.method == 'POST':
        if response['success']:
            return JsonResponse(response, safe=False)
    return JsonResponse(response, safe=False)

def login_get(request):
    response = {}
    response['type'] = 'login_get'
    if request.user.is_authenticated():
        response['user_logged_in'] = True
    else:
        response['user_logged_in'] = False
    return response

def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    response = {}
    response['type'] = 'login_post'
    if user is not None:
        login(request, user)
        request.session['username'] = username
        response['success'] = True
        response['message'] = "User login successful"
        return response
    else:
        response['success'] = False
        response['message'] = "Invalid username or password"
        return response

login_request_methods = {
    "POST" : login_post,
    "GET" : login_get
}

@csrf_exempt
def user_login(request):
    function = login_request_methods[request.method]
    response = function(request)
    if request.method == 'GET':
        if response['user_logged_in'] == True:
            return HttpResponseRedirect('/sellbuy/dashboard/')
        else:
            return render(request , 'LoginRegister/login.html')
    elif request.method == 'POST':
        if response['success']:
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse(response, safe=False)
    return JsonResponse(response, safe=False)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#def developers(request):
#    return render(request,'LoginRegister/developers.html')
