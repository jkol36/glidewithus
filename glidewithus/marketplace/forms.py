from glidewithus.profiles.models import GlideProfile, Interest, Company, Proffession
from django import forms 
from glidewithus.profiles.models import Interest, Company, Proffession

class filterbyinterestForm(forms.Form):
	interest_choices = Interest.objects.all()
	select_interest = forms.MultipleChoiceField(choices = interest_choices)

class filterbycompanyForm(forms.Form):
	company_choices = Company.objects.all()
	select_company = forms.MultipleChoiceField(label="select_company", choices = company_choices, required = False)

class filterbyprofessionForm(forms.Form):
	profession_choices = Proffession.objects.all()
	select_profession = forms.MultipleChoiceField(label="select_profession", choices = profession_choices, required = False)



class SearchLocationForm(forms.Form):
	location = forms.CharField(widget=forms.TextInput(attrs={'id':'location_search', 'class':'form-control'}))