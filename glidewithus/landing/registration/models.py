from django.db import models

# Create your models here.

class requested_invites(models.Model):
	email = models.EmailField(unique=True)
	mission_statement = models.CharField(max_length=750, null = True, blank = True)
	date_registered = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.email

	def get_mission_statement(self):
		return self.mission_statement
