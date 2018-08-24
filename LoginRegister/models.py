# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserDetail(models.Model):
  	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120,blank=False,null=False)
	username = models.CharField(max_length=120,blank=False,null=False, unique=True)
	college = models.CharField(max_length=120,blank=False,null=False)
	branch = models.CharField(max_length=120,blank=False,null=False)
	email = models.CharField(max_length=120,blank=False,null=False)
	contact = models.DecimalField(max_digits=11,decimal_places=0,blank=False,null=False)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name