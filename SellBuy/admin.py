# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Share, SharePrice, UserHolding, CurrentUserHolding, UserShareQuantity
from django.contrib import admin

# Register your models here.
class ShareAdmin(admin.ModelAdmin):
    list_display = ['name','current_price']
admin.site.register(Share,ShareAdmin)

class SharePriceAdmin(admin.ModelAdmin):
    list_display = ['__str__','price','time']
admin.site.register(SharePrice,SharePriceAdmin)

class UserHoldingAdmin(admin.ModelAdmin):
    list_display = ['__str__','holding','time']
admin.site.register(UserHolding,UserHoldingAdmin)

class CurrentUserHoldingAdmin(admin.ModelAdmin):
    list_display = ['__str__','current_holding']
admin.site.register(CurrentUserHolding,CurrentUserHoldingAdmin)

class UserShareQuantityAdmin(admin.ModelAdmin):
    list_display = ['__str__','share_name','share_price','quantity']
admin.site.register(UserShareQuantity,UserShareQuantityAdmin)    