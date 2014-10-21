from django.db import models
from glidewithus.profiles.models import GlideProfile
from django.utils import datetime

# Create your models here.

class Notification(models.Model):
	body = models.TextField(max_length = 50)
	notification_from = models.CharField(max_length = 100, blank = False, null = False, verbose_name = ('From'))
	notification_to = models.CharField(max_length = 100, blank = False, null = False, verbose_name = ('To'))
	date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return self.body