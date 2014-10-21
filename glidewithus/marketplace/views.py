from django.shortcuts import render
from forms import filterbyinterestForm, filterbycompanyForm, filterbyprofessionForm, SearchLocationForm

# Create your views here.

def marketplace(request):
	interests = request.user.glideprofile.interest_set.all()
	professions = request.user.glideprofile.proffession_set.all()
	companies = request.user.glideprofile.company_set.all()
	forms = {'interest_form':filterbyinterestForm, 'company_form':filterbycompanyForm, 'profession_form':filterbyprofessionForm, 'searchlocation':SearchLocationForm}
	if interests:
		form = filterbyinterestForm()
		return render(request, 'marketplace.jade', {'interests':interests, 'form':forms, 'companies':companies, 'professions':professions})
	else:
		form = filterbyinterestForm()
		return render(request, 'marketplace.jade', {'form':forms})
	if request.POST:
		form = SearchLocationForm(data = request.POST, instance = request.user.glideprofile )
		print request.POST