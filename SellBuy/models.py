# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Share(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120,blank=False,null=False)
	current_price = models.FloatField(default=1000.00)
	previous_price = models.FloatField(default=1000.00)

	def __str__(self):
		return str(self.name)

class SharePrice(models.Model):
	share = models.ForeignKey('Share')
	price = models.FloatField(default=1000.00)
	time = 	models.TimeField(auto_now=True)

	def __str__(self):
		return str(self.share.name)

class UserHolding(models.Model):
	user = models.ForeignKey(User)
	time = models.TimeField(auto_now=True)
	holding = models.FloatField(default=25000.00)

	def __str__(self):
		return self.user.username

class CurrentUserHolding(models.Model):
	user = models.ForeignKey(User)
	current_holding = models.FloatField(default=25000.00)

	def __str__(self):
		return self.user.username

class UserShareQuantity(models.Model):
	user = models.ForeignKey(User)
	share = models.ForeignKey('Share')
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

	def share_name(self):
		return self.share.name

	def share_price(self):
		return self.share.current_price		