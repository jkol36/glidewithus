from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Search(models.Model):
	interest = models.CharField(max_length = 250, null = True, blank = True)
	company = models.CharField(max_length = 250, null = True, blank = True)
	profession = models.CharField(max_length = 250, null = True, blank = True)
	keyword = models.CharField(max_length= 250,  null = True)

	def __unicode__(self):
		return "%s(%s)(%s)(%s)" %(self.interest, self.company, self.profession, self.keyword)
