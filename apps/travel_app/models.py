from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from ..login_register.models import User
from datetime import datetime as dt

class TripManager(models.Manager):
	def validate(self, userRequest, request):
		errors = False
		if len(userRequest['destination']) < 1:
			messages.add_message(request, messages.INFO, 'Must have Destination')
			errors = True
		if len(userRequest['start_date']) < 1:
			messages.add_message(request, messages.INFO, 'Must have Start Date')
			errors = True
		if len(userRequest['end_date']) < 1:
			messages.add_message(request, messages.INFO, 'Must have End Date')
			errors = True
		if len(userRequest['description']) <1:
			messages.add_message(request, messages.INFO, 'Must have Description')
			errors = True
		now = dt.now()
		now = now.strftime('%Y-%m-%d')
		a = dt.strptime(userRequest['start_date'], '%Y-%m-%d')
		b = dt.strptime(userRequest['end_date'], '%Y-%m-%d')
		now = dt.strptime(now, '%Y-%m-%d')
		if a > b:
			messages.add_message(request, messages.INFO, 'Start Date must be before End Date')
			errors = True
		if a < now:
			messages.add_message(request, messages.INFO, 'Start Date must be after Current Date')
			errors = True
		if errors == True:
			return False
		else:
			return True
# Create your models here.
class Trip(models.Model):
	author = models.ForeignKey(User, null=True, related_name='author')
	joiners = models.ManyToManyField(User, null=True, related_name='joiners')
	destination = models.CharField(max_length=45)
	start_date = models.CharField(max_length = 45,null=True)
	end_date = models.CharField(max_length = 45, null=True)
	description = models.CharField(max_length=140)

	tripManager = TripManager()
	objects = models.Manager()