from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AnonymousUser
from glidewithus.landing.registration.models import requested_invites
from glidewithus.landing.registration.forms import RequestInviteForm, UserForm, GlideProfileForm
from django.shortcuts import render, redirect
from glidewithus.profiles.models import GlideProfile


# Create your views here.

def landing(request):
	if request.method == "POST":
		form = RequestInviteForm(request.POST)
		if form.is_valid():
			email_address = form.cleaned_data['email_address']
			mission_statement = form.cleaned_data['mission_statement']
			new_registration = requested_invites(email=email_address, mission_statement=mission_statement)
			new_registration.save()
			return HttpResponse("Thank You. We'll be in touch.")
	
	registration_form = RequestInviteForm()
	return render(request, 'landing.jade', {'form':registration_form})
def home(request, registration_form):
	return render(request, 'landing.jade')
def signup(request):
	print request.user
	if request.POST:
		print request.POST
		form = UserForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			email_address = form.cleaned_data['email_address']
			beta_key = form.cleaned_data['beta_key']
			if beta_key != "LETS GLIDE":
				return HttpResponse('Beta Key wrong')
			elif password != password2:
				return HttpResponse("Passwords must match")
			user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email_address)
			gprofile = GlideProfile.objects.create(profile=user)
			gprofile.save()
			return redirect('profile')
		else:
			if "username" in form.errors:
				return HttpResponse('Username already taken.')
			
			
	elif request.user.is_anonymous():
		return render(request, 'signup.jade', {'user_form':UserForm, 'AnonymousUser':AnonymousUser})
	else:
		return redirect('profile')

	

def login(request):
	if request.method == 'POST':
		print request.POST
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			auth_login(request, user)
			return redirect('profile')
		return HttpResponse("Sorry, your login information is incorrect")

	return render(request, 'login.jade')


