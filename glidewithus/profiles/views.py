from django.shortcuts import render, redirect
import json
from django_ajax.decorators import ajax
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AnonymousUser 
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from models import GlideProfile, Interest, Proffession, Company
from forms import GlideProfileForm, UpdateUserForm, InterestForm, CompanyForm, ProfessionForm, LocationForm, awesomeform, travelform, missionform, UpdateUserNameForm, UpdatePasswordForm, UpdateEmailForm, UploadPicForm, ChangeProfilePictureForm
from glidewithus.marketplace.forms import filterbyinterestForm, filterbycompanyForm, filterbyprofessionForm, SearchLocationForm
from sorl.thumbnail import get_thumbnail
from glidewithus.marketplace.forms import filterbyinterestForm, filterbycompanyForm, filterbyprofessionForm, SearchLocationForm
from sorl.thumbnail import ImageField


# Create your views here.
@login_required
def edit_profile(request):
	return redirect('profiles.jade')

def profile(request):
	if not request.user.is_authenticated():
		try:
			return redirect('login')
		except Exception, e:
			print e

	elif request.user.glideprofile:
		interests = request.user.glideprofile.interest_set.all()
		proffession = request.user.glideprofile.proffession_set.distinct()
		company = request.user.glideprofile.company_set.distinct()
		city = request.user.glideprofile.city
		country = request.user.glideprofile.country
		state = request.user.glideprofile.state
		mission = request.user.glideprofile.mission_statement
		awesome = request.user.glideprofile.why_awesome
		traveler_pitch = request.user.glideprofile.traveler_pitch
		glideprofile = request.user.glideprofile
		forms = {'gprofileform':GlideProfileForm(), 'updateusername':UpdateUserForm, 'changepropic':ChangeProfilePictureForm, 'propic_form':UploadPicForm, 'locationform':LocationForm(), 'searchlocationform':SearchLocationForm, 'filterbyprofessionform':filterbyprofessionForm, 'filterbycompanyform':filterbycompanyForm, 'filterbyinterestform':filterbyinterestForm, 'missionform':missionform, 'updateuserform':UpdateUserForm(), 'interestform':InterestForm(), 'companyform':CompanyForm(), 'professionform':ProfessionForm, 'awesomeform':awesomeform, 'travelform':travelform}
		if request.method=='GET':
			try:
				interest_id = request.GET['interest']
				print "interest id %d" %interest_id
			except Exception, e:
				pass
		if request.POST:
			try:
				interests = request.user.glideprofile.interest_set.all()
				proffession = request.user.glideprofile.proffession_set.distinct()
				company = request.user.glideprofile.company_set.distinct()
				city = request.user.glideprofile.city
				country = request.user.glideprofile.country
				state = request.user.glideprofile.state
				mission = request.user.glideprofile.mission_statement
				awesome = request.user.glideprofile.why_awesome
				traveler_pitch = request.user.glideprofile.traveler_pitch
				forms = {'gprofileform':GlideProfileForm(), 'locationform':LocationForm(), 'searchlocationform':SearchLocationForm, 'filterbyprofessionform':filterbyprofessionForm, 'filterbycompanyform':filterbycompanyForm, 'filterbyinterestform':filterbyinterestForm, 'missionform':missionform, 'updateuserform':UpdateUserForm(), 'interestform':InterestForm(), 'companyform':CompanyForm(), 'professionform':ProfessionForm, 'awesomeform':awesomeform, 'travelform':travelform}
			
				if 'mission_statement' in request.POST:
					print dir(request.user)
					mission = request.user.glideprofile.mission_statement
					form = GlideProfileForm(request.POST, instance = request.user.glideprofile)
					if form.is_valid():
						mission_statement = form.cleaned_data['mission_statement'].__format__(mission_statement[0].uppercase())
						city = form.cleaned_data['city'].__format__(city[0].uppercase())
						state = form.cleaned_data['state']
						age = form.cleaned_data['age']
						country = form.cleaned_data['country']
						request.user.glideprofile.mission_statement = mission_statement
						request.user.glideprofile.country = country
						request.user.glideprofile.state = state
						request.user.glideprofile.city = city
						request.user.glideprofile.age = age
						request.user.glideprofile.save()
				
				elif "Interest_name" in request.POST:
					form = InterestForm(data = request.POST, instance = request.user.glideprofile)
					if form.is_valid():
						interest = form.cleaned_data["Interest_name"]


						#request.user.glideprofile.interest_set.get_or_create(name=formated_interest)
						#request.user.save()
						return redirect('profile')
				elif "Profession_Name" in request.POST:
					print request.POST
					form = ProfessionForm(data=request.POST, instance=request.user.glideprofile)

					if form.is_valid():
						new_occupation = form.cleaned_data['Profession_Name'].__format__(new_occupation[0].uppercase())
						print new_occupation
						if new_occupation in request.user.glideprofile.proffession_set.all():
							return HttpResponse("You already added a profession with this name")
						request.user.glideprofile.proffession_set.get_or_create(name=new_occupation)
						return redirect('profile')

				elif 'user_name' in request.POST:
					form = UpdateUserForm(data=request.POST, instance=request.user)
					if form.is_valid():
						username = form.cleaned_data['user_name']
						email_address = form.cleaned_data['email_address']
						last_name = form.cleaned_data['last_name']
						first_name = form.cleaned_data['first_name']
						request.user.username=username
						request.user.email=email_address
						request.user.last_name = last_name
						request.user.first_name = first_name
						request.user.save()

				elif 'company_name' in request.POST:
					form = CompanyForm(data=request.POST, instance=request.user.glideprofile)
					if form.is_valid():
						new_company = form.cleaned_data['company_name'].__format__(new_company[0].uppercase())
						request.user.glideprofile.company_set.get_or_create(name=new_company)
						form.save()
						return redirect('profile')
			

				elif "city" in request.POST:
					form = LocationForm(data = request.POST, instance = request.user.glideprofile)
					print form.errors
					if form.is_valid():
						city = form.cleaned_data['city'].__format__(city[0].uppercase())
						country = form.cleaned_data['country']
						state = form.cleaned_data['state']
						request.user.glideprofile.city = city
						request.user.glideprofile.country = country
						request.user.glideprofile.state= state
						form.save()
						return redirect('profile')

				elif 'edit_awesome' in request.POST:
					print request.POST
					form = awesomeform(data=request.POST, instance=request.user.glideprofile)
					if form.is_valid():
						edited_awesome = form.cleaned_data['edit_awesome'].__format__(edited_awesome[0].uppercase())
						request.user.glideprofile.why_awesome = edited_awesome
						form.save()
						return redirect('profile')
					else:
						print form.errors

				elif 'edit_travelform' in request.POST:
					form = travelform(data=request.POST, instance=request.user.glideprofile)
					if form.is_valid():
						text = form.cleaned_data['edit_travelform'].__format__(text[0].uppercase())
						request.user.glideprofile.traveler_pitch = text
						form.save()
						return redirect('profile')
					else:
						print form.errors
				elif 'edit_mission' in request.POST:
					form = missionform(data= request.POST, instance=request.user.glideprofile)
					if form.is_valid():
						mission = form.cleaned_data['edit_mission'].__format__(mission[0].uppercase())
						request.user.glideprofile.mission_statement = mission
						form.save()
						return redirect('profile')
				elif 'profile_pic' in request.FILES:
					form = UploadPicForm(request.POST, request.FILES)
					if form.is_valid():
						profile = request.user.glideprofile
						profile.profile_pic = request.FILES['profile_pic']
						profile.save()
			except Exception, e:
				print e


	return render(request, 'profiles.jade', {'form':forms, 'interests':interests, 'profile':glideprofile, 'proffession':proffession, 'company':company, 'mission':mission, 'awesome':awesome, 'traveler_pitch': traveler_pitch, 'city':city,'state':state, 'country':country})
	

@login_required
def logout_view(request):
	logout(request)
	return redirect('landing')
	
@login_required
def settings(request):
	username = request.user.username
	email = request.user.email
	forms = {'updateusername':UpdateUserNameForm(), 'updatepassword':UpdatePasswordForm(), 'updatemail':UpdateEmailForm()}
	if 'new_username' in request.POST:
		form = UpdateUserNameForm(data = request.POST, instance=request.user)
		if form.is_valid():
			try:
				username = form.cleaned_data['new_username']
				request.user.username=username
				form.save() 
			except Exception, e:
				print e
		else:
			print "form has errors"
	elif 'new_password' in request.POST:
		form = UpdatePasswordForm(data = request.POST, instance = request.user)
		if form.is_valid():
			try:
				user = authenticate(username=request.user.username, password=form.cleaned_data['old_password'])
				if user is not None:
					print "authenticated"
					try:
						new_password = form.cleaned_data['new_password']
						print new_password
						new_password_again = form.cleaned_data['new_password_again']
						print new_password_again
						if new_password == new_password_again:
							np = new_password
							user = request.user.set_password(np)
							user.save()
							form.save()
						return 
					except Exception, e:
						print e
				else:
					print "You entered the wrong password for your account"
			except Exception, e:
				print e
		else:
			print "form is invalid"
	elif 'new_email' in request.POST:
		print request.POST
		form = UpdateEmailForm(data = request.POST, instance = request.user)
		if form.is_valid():
			try:
				new_email = form.cleaned_data['new_email']
				if new_email != request.user.email:
					request.user.email = new_email
					form.save()
				else:
					print "That's already your email"
			except Exception, e:
				print e
		else:
			print form.errors





	return render(request, 'settings.jade', {'username': username, 'email':email, 'form':forms})

@login_required
@ajax
def removeinterest(request):
	return {'result':'hello!'}

		

