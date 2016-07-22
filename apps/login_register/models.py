from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
MESSAGE_TAGS = {
	messages.INFO: '',
	1: 'register'
}
# Create your models here.
class UserManager(models.Manager):
	def validateRegister(self, userRequest, request):
		errors = False
		register = 10
		if len(userRequest['name']) < 3:
			messages.add_message(request, messages.INFO, 'Name is too short')
			errors = True
		if len(userRequest['username']) < 3:
			messages.add_message(request, messages.INFO, 'Username must be at least 3 characters')
			errors = True
		if User.objects.filter(username=userRequest['username']).count() > 0:
			messages.add_message(request, messages.INFO, 'Username is taken')
			errors = True
		if len(userRequest['password']) < 8:
			messages.add_message(request, messages.INFO, 'Password is too short')
			errors = True
		if userRequest['password'] != userRequest['confirm_password']:
			messages.add_message(request, messages.INFO, 'Passwords do not match')
			errors = True

		if errors == True:
			return False
		else:
			return True

	def validateLogin(self, userRequest, request):
		errors = False
		password = userRequest['password']
		password = password.encode(encoding='utf-8', errors='strict')
		userExist = User.objects.filter(username = userRequest['username'])
		if not userExist.count():
			messages.add_message(request, messages.INFO, 'Username is not registered')
			return False
		else:
			checkUser = User.objects.get(username = userRequest['username'])
			if bcrypt.hashpw(password, checkUser.pwhash.encode(encoding='utf-8', errors='strict')) != checkUser.pwhash.encode(encoding='utf-8', errors='strict'):
				messages.add_message(request, messages.INFO, 'Incorrect Password')
				return False
			else: 
				return True	
			

	def register(self, userRequest, request):
		password = self.hashPassword(userRequest['password'])
		
		User.objects.create(name = userRequest['name'], username=userRequest['username'], pwhash=password)
	def login(self, userRequest, request):
		currentUser = User.objects.get(username = userRequest['username'])
		request.session['username'] = currentUser.username
		request.session['name'] = currentUser.name
		request.session['id'] = currentUser.id


	def hashPassword(self,password):
		preliminaryHash = password.encode(encoding='utf-8', errors='strict')
		pwhash = bcrypt.hashpw(preliminaryHash,bcrypt.gensalt())
		return pwhash
class User(models.Model):
	name = models.CharField(max_length=(45))
	username = models.CharField(max_length=(45))
	pwhash = models.CharField(max_length=(255))

	userManager = UserManager()
	objects = models.Manager()