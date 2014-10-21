from django.contrib.auth.models import User
from models import GlideProfile, Interest, Company, Proffession
from django import forms
from sorl.thumbnail import ImageField
from glidewithus.profiles.countries import COUNTRIES
from glidewithus.profiles.states import STATES

class GlideProfileForm(forms.ModelForm):
	mission_statement = forms.CharField(label="mission statement", widget=forms.Textarea(attrs={'id':'mission_statement', 'class':'form-control', 'placeholder':'Your mission statement should explain what drives you.', 'rows':5}))
	country = forms.ChoiceField(choices=COUNTRIES, label="What country do you reside in?")
	state = forms.ChoiceField(choices=STATES, label="What state are you from?")
	city = forms.CharField(label="city", widget=forms.TextInput(attrs={'id':'City', 'class':'form-control', 'placeholder':'Your current City' }))
	age = forms.DateField(label="age", widget=forms.TextInput(attrs={'id':'Age', 'class':'form-control', 'placeholder':'your age'}))
	class Meta:
		model = GlideProfile
		fields = ['mission_statement', 'country', 'state', 'city', 'age']

class InterestForm(forms.ModelForm):
	Interest_name = forms.CharField(label="Add a new interest", widget=forms.TextInput(attrs={'id':'interest_name', 'class':'form-control','placeholder':'New Interest Name'}))

	class Meta:
		model = Interest
		fields = ['Interest_name']
class CompanyForm(forms.ModelForm):
	company_name = forms.CharField(label="Add New Company", widget=forms.TextInput(attrs={'id':'company_name', 'class':'form-control', 'placeholder':'Add a new Company'}))

	class Meta:
		model = Company
		fields = ['company_name']

class ProfessionForm(forms.ModelForm):
	Profession_Name = forms.CharField(label="new profession", widget=forms.TextInput(attrs={'id':'new_proffesion', 'class':'form-control', 'placeholder':'new profession'}))

	class Meta:
		model = Proffession
		fields = ['Profession_Name']

class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(label="first name", widget=forms.TextInput(attrs={'id':'first_name', 'class':'form-control', 'placeholder':'Your First Name'}))
	last_name = forms.CharField(label="last name", widget=forms.TextInput(attrs={'id':'last_name', 'class':'form-control', 'placeholder':'Your Last Name'}))
	email_address = forms.CharField(label="email_address", widget=forms.EmailInput(attrs={'id':'email_address', 'class':'form-control', 'placeholder':'Update your Email Address'}))
	user_name = forms.CharField(label="username", widget=forms.TextInput(attrs={'id':'username', 'class':'form-control', 'placeholder':'update username'}))

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email_address','user_name']


class LocationForm(forms.ModelForm):
	city = forms.CharField(label="Edit City", widget=forms.TextInput(attrs={"id":'City', 'class':'form-control', 'placeholder':'new city name',}))
	state = forms.ChoiceField(label="Edit State", choices=STATES)
	country = forms.ChoiceField(label="Edit Country", choices=COUNTRIES)

	class Meta:
		model = GlideProfile
		fields = ['city', 'state', 'country']

class awesomeform(forms.ModelForm):
	edit_awesome = forms.CharField(label="Change why you're awesome", widget=forms.Textarea(attrs={'id':'Awesome_Field', 'class':'form-control', 'placeholder':"I'm awesome because I love meeting new people!"}))

	class Meta:
		model = GlideProfile
		exclude = ['mission_statement', 'city', 'age', 'country', 'state']
		fields = ['edit_awesome']

class travelform(forms.ModelForm):
	edit_travelform = forms.CharField(label="Why would a traveler want to meet up with you?", widget=forms.Textarea(attrs={'id':'travel_field', 'class':'form-control', 'placeholder':'Because...I can show them to the best bars and restaurants.'}))

	class Meta:
		model = GlideProfile
		exclude = ['mission_statement', 'city', 'country', 'age', 'state'] 
		fields = ['edit_travelform']

class missionform(forms.ModelForm):
	edit_mission = forms.CharField(label="Change your mission statement", widget=forms.Textarea(attrs={'id':'miission_form', 'class':'form-control', 'placeholder': 'mission statement'}))

	class Meta:
		model= GlideProfile
		exclude = ['city', 'state', 'age', 'country']
		fields = ['edit_mission']
