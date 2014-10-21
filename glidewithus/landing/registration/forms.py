from models import requested_invites
from django.contrib.auth.models import User
from glidewithus.profiles.models import GlideProfile
from django import forms

class RequestInviteForm(forms.ModelForm):
	email_address = forms.CharField(widget=forms.EmailInput(attrs={'id':'RequestInviteEmail', 'class':'form-control', 'placeholder':'Enter your email address'}))
	mission_statement = forms.CharField(label="What's your mission statement?", widget=forms.Textarea(attrs={'id':'RequestInviteMissionStatement', 'class':'form-control', 'placeholder': "A misision statement is a firm ", 'rows':5,}))

	class Meta:
		model = requested_invites
		fields=('email_address', 'mission_statement')


class UserForm(forms.ModelForm):
	first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'id':'first_name', 'class':'form-control', 'placeholder':'Jon'}))
	last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'id':'last_name', 'class':'form-control', 'placeholder':'Doe'}))
	username = forms.CharField(label="Username", widget =forms.TextInput(attrs={'id':'SignUpUsername', 'class':'form-control', 'placeholder':'Your Username'}))
	password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id':'SignUpPassword1', 'class':'form-control', 'placeholder':'Enter a secure Passsword'}))
	password2 = forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs={'id':'SignUpPassword2', 'class':'form-control', 'placeholder':'Enter Password Again'}))
	email_address = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'id':'SignUpEmail', 'class':'form-control', 'placeholder':'Enter your email'}))
	beta_key = forms.CharField(label="Beta Key", widget=forms.TextInput(attrs={'id':'SignUpBetaKey', 'class':'form-control', 'placeholder':'enter the beta key you recieved by email'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email_address', 'password', 'password2','beta_key')

class GlideProfileForm(forms.ModelForm):
	mission_statement = forms.CharField(label="What are you passionate about?")
	location = forms.CharField(label="Where do you reside?")

	class Meta:
		model = GlideProfile
		fields = ('mission_statement', 'location')

