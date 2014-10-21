from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from models import GlideProfile, Interest, Proffession, Company
from forms import GlideProfileForm, UpdateUserForm, InterestForm, CompanyForm, ProfessionForm, LocationForm, awesomeform, travelform, missionform
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
			forms = {'gprofileform':GlideProfileForm(), 'locationform':LocationForm(), 'missionform':missionform, 'updateuserform':UpdateUserForm(), 'interestform':InterestForm(), 'companyform':CompanyForm(), 'professionform':ProfessionForm, 'awesomeform':awesomeform, 'travelform':travelform}
			if request.POST:
				if 'mission_statement' in request.POST:
					print dir(request.user)
					mission = request.user.glideprofile.mission_statement
					form = GlideProfileForm(request.POST, instance = request.user.glideprofile)
					if form.is_valid():
						mission_statement = form.cleaned_data['mission_statement']
						city = form.cleaned_data['city']
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
					print request.POST
					form = InterestForm(data = request.POST, instance = request.user.glideprofile)
					if form.is_valid():
						new_interest = form.cleaned_data['Interest_name']
						request.user.glideprofile.interest_set.get_or_create(name=new_interest)
						request.user.save()
						return redirect('profile')
				elif "Profession_Name" in request.POST:
					print request.POST
					form = ProfessionForm(data=request.POST, instance=request.user.glideprofile)

					if form.is_valid():
						new_occupation = form.cleaned_data['Profession_Name']
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
						new_company = form.cleaned_data['company_name']
						request.user.glideprofile.company_set.get_or_create(name=new_company)
						form.save()
						return redirect('profile')
			

				elif "city" in request.POST:
					form = LocationForm(data = request.POST, instance = request.user.glideprofile)
					print form.errors
					if form.is_valid():
						city = form.cleaned_data['city']
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
						edited_awesome = form.cleaned_data['edit_awesome']
						request.user.glideprofile.why_awesome = edited_awesome
						form.save()
						return redirect('profile')
					else:
						print form.errors

				elif 'edit_travelform' in request.POST:
					form = travelform(data=request.POST, instance=request.user.glideprofile)
					if form.is_valid():
						text = form.cleaned_data['edit_travelform']
						request.user.glideprofile.traveler_pitch = text
						form.save()
						return redirect('profile')
					else:
						print form.errors
				elif 'edit_mission' in request.POST:
					form = missionform(data= request.POST, instance=request.user.glideprofile)
					if form.is_valid():
						mission = form.cleaned_data['edit_mission']
						request.user.glideprofile.mission_statement = mission
						form.save()
						return redirect('profile')

		except Exception, e:
			return e
		print city
		print awesome
		return render(request, 'profiles.jade', {'form':forms, 'interests':interests, 'proffession':proffession, 'company':company, 'mission':mission, 'awesome':awesome, 'traveler_pitch': traveler_pitch, 'city':city,'state':state, 'country':country})


def logout_view(request):
	logout(request)
	return redirect('landing')
	

def interest_initial(request):
	pass

		

