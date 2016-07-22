from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from ..login_register.models import User
from models import Trip
# Create your views here.
def travel(request):
	context ={
		'User' : User.objects.get(username=request.session['username']),
		'Trip' : Trip.objects.all(),
	}
	return render(request, 'travel_app/travel.html', context)
def add_plan(request):
	return render(request, 'travel_app/add_plan.html')
def add_plan_process(request):
	id = request.POST['author_id']
	user = User.objects.get(id=id)
	userRequest = {
		'destination' : request.POST['destination'],
		'start_date' : request.POST['start_date'],
		'end_date' : request.POST['end_date'],
		'description' : request.POST['description'],
	}
	if Trip.tripManager.validate(userRequest, request) == True:
		Trip.objects.create(destination = request.POST['destination'], start_date = request.POST['start_date'], end_date = request.POST['end_date'], author=user, description=request.POST['description'])
		return redirect(reverse('travel'))
	else: 
		return redirect(reverse('add_plan'))
def destination(request, id):
	context ={
		'Trip' : Trip.objects.get(id=id),
		'User' : User.objects.all(),
	}
	return render(request, 'travel_app/destination.html', context)
def join(request):
	trip = Trip.objects.get(id=request.POST['trip_id'])
	user = User.objects.get(id=request.POST['user_id'])
	trip.joiners.add(user)
	return redirect(reverse('destination', kwargs={'id':request.POST['trip_id']}))