from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
	meetup_request = meetuprequest(target_recipient=request.user.glideprofile)
	senders = []
	recipient = meetup_request.get_recipient()
	sender_object = meetuprequest.objects.filter(target_recipient=request.user.glideprofile)
	forms = {'company_form':filterbycompanyForm, 'meetup_form':sendmeetrequestForm, 'profession_form':filterbyprofessionForm, 'searchlocation':SearchLocationForm, 'search_interest':filterbyinterestForm}
	if interests:
		if request.POST:
			senders = []

			if 'location' in request.POST:
				location = request.POST['location']
				result_count = len(GlideProfile.objects.filter(city_icontains=location))
				matches = GlideProfile.objects.filter(city_icontains=location)
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
				matches = GlideProfile.objects.filter
				print dir(matches)
				results = []
				for i in matches:
					results.append(i)
				return render(request, 'marketplace.jade', {'results':results})
			elif 'view all' in request.POST:
				result_count = len(GlideProfile.objects.all())
				matches = GlideProfile.objects.all().exclude(profile=request.user)
				results = []
				count = 0
				while matches and count < result_count:
					try:
						results.append(matches[count])
					except Exception, e:
						return e

				return render(request, 'marketplace.jade', {'results':results, 'form':forms})
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
				location = request.POST['location']
				result_count = len(GlideProfile.objects.filter())
				matches = GlideProfile.objects.filter(city__icontains=location)
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
				print result_count
				matches = GlideProfile.objects.all().exclude(profile=request.user)
				results = []
				count = 0
				while matches:
					try:
						results.append(matches[count])
						count+=1
					except Exception, e:
						count = len(matches)-1
						break

					
			return render(request, 'marketplace.jade', {'form':forms, 'results':results})
		return render(request, 'marketplace.jade', {'form':forms})
	
	
