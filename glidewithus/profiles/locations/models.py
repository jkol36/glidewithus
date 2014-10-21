from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length = 100, unique = True, blank = False)
	state = models.CharField(max_length = 100, unique = True, blank = False, default = None)
	country = models.CharField(max_length = 100, default = None, blank = False)
	has_local = models.BooleanField(default = False)
	total_locals = models.IntegerField(max_length = None, default = None, blank = True)

	def __unicode__(self):
		return self.name

	def get_state(self):
		return __unicode__(self.state)

	def get_country(self):
		return __unicode__(self.country)

	def get_locals(self):
		if self.has_local == True:
			return 'has locals'
		else:
			return 'No locals'

