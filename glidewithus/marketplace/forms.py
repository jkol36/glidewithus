from glidewithus.profiles.models import GlideProfile, Interest, Company, Proffession
from django import forms
from django.forms import ModelChoiceField 
from glidewithus.profiles.models import Interest, Company, Proffession
from glidewithus.marketplace.models import Search


class filterbyinterestForm(forms.ModelForm):
	interest_name = forms.CharField(max_length=250, label="Enter a interest name", widget=forms.TextInput(attrs={'id':'interest_input_search', 'class':'form-control', 'placeholder':'I.E, Entrepreneurship'}))

	class Meta:
		model = Search
		fields = ["interest_name"]

class filterbycompanyForm(forms.ModelForm):
	company_name = forms.CharField(max_length=250, label="Enter the name of a company", widget=forms.TextInput(attrs={'id':'company_input_search', 'class':'form-control', 'placeholder':'I.E, Google'}))

	class Meta:
		model = Search
		fields = ["company_name"]

class filterbyprofessionForm(forms.Form):
	profession_name = forms.CharField(max_length = 250, label="Profession", widget=forms.TextInput(attrs={'id':'profession_search', 'class':'form-control', 'placeholder':'I.E, Doctor'}))

	class Meta:
		model = Search
		fields = ['profession_name']

class SearchLocationForm(forms.Form):
	location = forms.CharField(widget=forms.TextInput(attrs={'id':'location_search', 'class':'form-control'}))


