from django.db import models
from django.contrib.auth.models import User
from glidewithus.profiles.models import GlideProfile


# Create your models here.

class meetuprequest(models.Model):
	seen = models.BooleanField(default=False)
	target_sender = models.ForeignKey(GlideProfile, verbose_name="Booking Initiator", related_name="book_senders")
	target_recipient = models.ForeignKey(GlideProfile, verbose_name = "Booking Recipient", related_name = "book_recipients")
	start_time = models.TimeField(null = True)
	date = models.DateField()
	message = models.TextField()
	response = models.NullBooleanField(null=True)

	def __unicode__(self):
		return self.target_sender.get_full_name()

	def get_sender(self):
		return self.target_sender.get_full_name()

	def get_recipient(self):
		return self.target_recipient.get_full_name()



