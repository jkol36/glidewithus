from django import forms
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import AuthenticationForm

class RegisterLandingPage(forms.ModelForm):
	username = forms.CharField(label="username")
	email = forms.CharField(label="email")
	password = forms.CharField(label="Password1")
	password2 = forms.CharField(label=_('Password2'))

 	class Meta:
 		model = User
 		fields = ('username', 'email', 'password', 'password2')
 	def Save(self, commit = True):
 		user = super(RegisterLandingPage, self).save(commit=False)
 		user.firstname = user.get['username']
 		user.email = user.get['email']
 		user.password = user.get['password']
 		if commit:
 			profile(user=user)  
 			user.save()
 			return User

class UserCreationForm(forms.ModelForm):

	error_messages = {'Duplicate_Username': _('A user with that username already exists'), 'password_mismatch': _("your password's do not match"),}
	username = forms.RegexField(label=_('Username'), max_length = 30,
		regex=r'^[\w.@+-]+$',
		help_text = _("Required. 30 character or more for username and @/./+/-/_ only. "),
		error_messages = {'invalid': _('This value may only contain letters and numbers')})
	password1= forms.CharField(label=("password"),
		widget = forms.PasswordInput)

	password2 = forms.CharField(label=("Password Confirmation"),
		widget = forms.PasswordInput,
		help_text = _('Enter the same password twice. Case Sensitive.'))

		class Meta:
			model = User
			fields = ("username")

			def clean_username(self):
				username = self.cleaned_data["username"]
				try:
					User.default_manager.get(username)

				except User.DoesNotExist:
					return username
				raise forms.ValidationError(self.error_messages['Duplicate_Username'], code="duplicate username", )

			def clean_password2(self):
				password1 = self.cleaned_data.get('password1')
				password2 = self.cleanred_data.get('password2')

				if password1 and password2 and password1 != password2:
					raise forms.ValidationError(self.error_messages['password_mismatch'], code = "password_mismatch")
				else:

					return password2

			def save(self, commit=True):
				user = super(UserCreationForm).save(commit=False)
				user.set_password(self.cleaned_data['password1'])
				if commit:
					user.save()
				return user


