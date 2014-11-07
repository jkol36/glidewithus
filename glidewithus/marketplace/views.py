<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
=======
from django.shortcuts import render
>>>>>>> f655b4bd88bb89dc9c671015128227aab0b56400
from glidewithus.profiles.models import GlideProfile
from forms import filterbyinterestForm, filterbycompanyForm, filterbyprofessionForm, SearchLocationForm
from glidewithus.booking.forms import sendmeetrequestForm
from glidewithus.booking.models import meetuprequest

# Create your views here.
@login_required
def marketplace(request):
	interests = request.user.glideprofile.interest_set.all()
	professions = request.user.glideprofile.proffession_set.all()
	companies = request.user.glideprofile.company_set.all()
<<<<<<< HEAD
	meetup_request = meetuprequest(target_recipient=request.user.glideprofile)
	senders = []
	recipient = meetup_request.get_recipient()
	sender_object = meetuprequest.objects.filter(target_recipient=request.user.glideprofile)
	print sender_object
	def get_interests(self):
		interests = self.user.glideprofile.interest_set.all()
		if interests:
			return interests
		else:
			return None
	def get_professions(self):
		professions = self.user.glideprofile.proffession_set.all()
		if proffessions:
			return professions
		else:
			return None
	def get_companies(self):
		companies = self.glideprofile.objects.company_set.all()
		if companies:
			return companies
		else:
			return None
	def get_meetup_requests(self):
		meetup_request = meetuprequest(target_recipient=self.user.glideprofile)
		recipient = meetup_request.get_recipient() #We want to get the recipient to make sure recipient is also the owner of the profile.
		sender_object = meetuprequest.objects.filter(target_recipient=self.user.glideprofile)
		return "%s"("%s")("%s") %(meetup_request, recipient, sender_object)



	forms = {'company_form':filterbycompanyForm, 'meetup_form':sendmeetrequestForm, 'profession_form':filterbyprofessionForm, 'searchlocation':SearchLocationForm, 'search_interest':filterbyinterestForm}
	if interests:
		if request.POST:
			senders = []

=======
	forms = {'company_form':filterbycompanyForm, 'profession_form':filterbyprofessionForm, 'searchlocation':SearchLocationForm, 'search_interest':filterbyinterestForm}
	if interests:
		if request.POST:
>>>>>>> f655b4bd88bb89dc9c671015128227aab0b56400
			if 'location' in request.POST:
				location = request.POST['location']
				result_count = len(GlideProfile.objects.filter(city=location))
				matches = GlideProfile.objects.filter(city=location)
				results = []
<<<<<<< HEAD
				results_list_one = []
				results_list_two = []
				companies = []
				count = 0
				for match in matches:
					if count < len(matches):
						results_list_one.append(matches[count])
						count+=1
						if count < len(matches):
							results_list_two.append(matches[count])
							count+=1
				list = zip(results_list_one, results_list_two)
				return render(request, 'marketplace.jade', {'results': list, 'form':forms})

=======
				for i in matches:
					results.append(i)
				return render(request, 'marketplace.jade', {'results': results})
>>>>>>> f655b4bd88bb89dc9c671015128227aab0b56400
			elif 'company_name' in request.POST:
				company_name = request.POST['company_name']
				result_count = len(GlideProfile.objects.filter(company=company_name))
				matches = GlideProfile.objects.filter(company=company_name)
				results = []
				for i in matches:
					results.append(i)
				return render(request,'marketplace.jade', {'results':results})
			elif 'profession_name' in request.POST:
				profession_name = request.POST['profession_name']
				result_count = len(GlideProfile.objects.filter(Proffession=profession_name))
				matches = GlideProfile.objects.filter(Proffession=profession_name)
				results = []
				for i in matches:
					results.append(i)
				return render(request, 'marketplace.jade', {'results':results})
			elif 'interest_name' in request.POST:
				interest_name = request.POST['interest_name']
<<<<<<< HEAD
				matches = GlideProfile.objects.filter
				print dir(matches)
				results = []
				for i in matches:
					results.append(i)
				return render(request, 'marketplace.jade', {'results':results})
			elif 'view all' in request.POST:
				result_count = len(GlideProfile.objects.all())
				matches = GlideProfile.objects.all()
				results = []
				results_list_one = []
				results_list_two = []
				count = 0
				for match in matches:
					if count < len(matches):
						results_list_one.append(matches[count])
						count+=1
						if count < len(matches):
							results_list_two.append(matches[count])
							count+=1
				list = zip(results_list_one, results_list_two)
				return render(request, 'marketplace.jade', {'results':list, 'form':forms})
			elif 'send_meetup_request' in request.POST:
				sender = request.user.username
				reciever = request.POST['send_to']
				if sender != reciever:
					message = request.POST['message']
					date = request.POST['date']
					if date and message:
						month = date[0:2]
						day = date[3:5]
						year = date[6:10]
						format_date = "%s-%s-%s" %(year, month, day)
						sender_user = User.objects.get(username=sender)
						GlideProfile_instance_of_sender = GlideProfile.objects.get(profile=sender_user)
						recipient_user = User.objects.get(username=reciever)
						recipient_gprofile = GlideProfile.objects.get(profile=recipient_user)
						new_meetup = meetuprequest(seen=False, target_sender=GlideProfile_instance_of_sender, message=message, target_recipient=recipient_gprofile, date=format_date)
						new_meetup.save()

		return render(request, 'marketplace.jade', {'interests':interests, 'recipient':recipient, 'sender':sender_object, 'form':forms, 'companies':companies, 'professions':professions})
	else:
		if request.POST:
			if 'location' in request.POST:
				print 'location in request.post'
				location = request.POST['location'.lower()]
				result_count = len(GlideProfile.objects.filter(city=location))
				matches = GlideProfile.objects.filter(city=location)
				results = []
				results_list_one = []
				results_list_two = []
				companies = []
				count = 0
				for match in matches:
					if count < len(matches):
						results_list_one.append(matches[count])
						count+=1
						if count < len(matches):
							results_list_two.append(matches[count])
							count+=1
				list = zip(results_list_one, results_list_two)
				return render(request, 'marketplace.jade', {'results': list, 'form':forms})
			elif 'view all' in request.POST:
				print request.POST
				result_count = len(GlideProfile.objects.all())
				matches = GlideProfile.objects.all()
				results_list_one = []
				result_list_two = []
				results = []
				companies = []
				for i in matches:
					results.append(i)
				print "result list one. Should have 50 percent more results than result list two"
				print "result one %s" %(result_list_one)
				print "result two %s"%(result_list_two)
			return render(request, 'marketplace.jade', {'form':forms, 'results':results})
		return render(request, 'marketplace.jade', {'form':forms})
	
	
=======
				matches = GlideProfile.objects.filter(interest="Hacker")
				print matches
				results = []
				for i in results:
					results.append(i)
				return render(request, 'marketplace.jade', {'results':results})
		return render(request, 'marketplace.jade', {'interests':interests, 'form':forms, 'companies':companies, 'professions':professions})
	else:
		if request.POST:
			print request.POST
		return render(request, 'marketplace.jade', {'form':forms})
	
>>>>>>> f655b4bd88bb89dc9c671015128227aab0b56400
