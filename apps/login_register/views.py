from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import User
# Create your views here.
def index(request):
	return render(request, 'login_register/index.html')
def register(request):
	print 'made it to register'
	userRequest = {
		'name': request.POST['name'],
		'username': request.POST['username'],
		'password': request.POST['password'],
		'confirm_password': request.POST['confirm_password']
	}
	# runs validation in model
	success = User.userManager.validateRegister(userRequest, request)
	if success == True:
		print 'register successful'
		User.userManager.register(userRequest, request)
		User.userManager.login(userRequest, request)
		return redirect(reverse('travel'))
	else:
		# returns to index.html
		print 'register failed'
		return redirect(reverse('index'))
	
	
	
def login(request):
	# runs validation in model
	userRequest = {
		'username' : request.POST['username'],
		'password' : request.POST['password'],
	}
	success = User.userManager.validateLogin(userRequest, request)
	if success == True:
		# sets session to user
		print 'login successful'
		User.userManager.login(userRequest, request)
		return redirect(reverse('travel'))
	else:
		# returns to index.html
		print 'login failed'
		return redirect(reverse('index'))
def logout(request):
	request.session['username'] = None
	request.session['name'] = None
	# redirect to loginRegisterPage
	return render(request, 'login_register/index.html')