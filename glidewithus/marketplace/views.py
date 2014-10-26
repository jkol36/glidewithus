from django.shortcuts import render
from glidewithus.profiles.models import GlideProfile
from forms import filterbyinterestForm, filterbycompanyForm, filterbyprofessionForm, SearchLocationForm

# Create your views here.

def marketplace(request):
	interests = request.user.glideprofile.interest_set.all()
	professions = request.user.glideprofile.proffession_set.all()
	companies = request.user.glideprofile.company_set.all()
	forms = {'company_form':filterbycompanyForm, 'profession_form':filterbyprofessionForm, 'searchlocation':SearchLocationForm, 'search_interest':filterbyinterestForm}
	if interests:
		if request.POST:
			if 'location' in request.POST:
				location = request.POST['location']
				result_count = len(GlideProfile.objects.filter(city=location))
				matches = GlideProfile.objects.filter(city=location)
				results = []
				for i in matches:
					results.append(i)
				return render(request, 'marketplace.jade', {'results': results})
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
	