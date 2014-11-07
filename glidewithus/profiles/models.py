from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from glidewithus.profiles.countries import COUNTRIES
from glidewithus.profiles.states import STATES
from sorl.thumbnail import ImageField

# Create your models here.

class GlideProfile(models.Model):
	profile = models.OneToOneField(User, unique = True)
	traveler_pitch = models.CharField(max_length=250, blank = True, null = True, default = None)
	profile_pic = ImageField(upload_to="images/profile_pics", default = None, null = True, blank = True) 
	why_awesome = models.CharField(max_length = 250, blank = True, null = True, default = None)
	mission_statement = models.CharField(max_length = 250, null=True, blank = True, default = None)
	country = models.CharField(max_length=2, choices=COUNTRIES, blank=True, null=True)
	state = models.CharField(max_length = 2, choices =STATES, blank = True, null=True)
	age = models.DateField(default = None, blank = True, null = True, verbose_name = 'age')
	city = models.CharField(max_length = 250, default = False, blank = True, verbose_name="City", null=True)
	has_profile_pic = models.BooleanField(default = False)
	is_entrepreneur = models.BooleanField(default=False)
	is_startup_founder = models.BooleanField(default = False)
	is_local = models.BooleanField(default = True)
	isfacebook_user = models.BooleanField(default = False)
	istwitter_user = models.BooleanField(default = False)

	def __unicode__(self):
<<<<<<< HEAD
		return "%s(%s)(%s)(%s)(%s)(%s)(%s)" %(self.profile.first_name, self.mission_statement, self.traveler_pitch, self.why_awesome, self.city, self.country, self.state)

	def get_full_name(self):
		return self.profile.first_name
=======
		return "%s(%s)(%s)(%s)(%s)(%s)(%s)" %(self.profile.first_name, self.mission_statement, self.traveler_pitch, self.why_awesome, self.city, self.country, self.state )
>>>>>>> f655b4bd88bb89dc9c671015128227aab0b56400

class Proffession(models.Model):
	user = models.ManyToManyField(GlideProfile)
	name = models.CharField(max_length = 300, default = None, blank = True)

	def __unicode__(self):
		return self.name



class Interest(models.Model):
	user = models.ManyToManyField(GlideProfile)
	name = models.CharField(max_length = 250, default = None, blank = True)

	def __unicode__(self):
		return self.name

class Company(models.Model):
	user = models.ManyToManyField(GlideProfile)
	name = models.CharField(max_length = 250, default = None, blank = True)

	def __unicode__(self):
		return self.name







