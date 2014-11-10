from django.db import models
from glidewithus.profiles.models import GlideProfile

# Create your models here.
class message(models.Model):
	sender = models.ForeignKey(GlideProfile, related_name = "sent_messages", verbose_name="Sender")
	recipient = models.ForeignKey(GlideProfile, related_name= "recieved_messages", verbose_name = "Reciever")
	sent_at = models.DateTimeField(auto_now_add = True)
	seen = models.NullBooleanField(default = False)

	def __unicode__(self):
		return self.target_sender.get_full_name()

	def get_recipient(self):
		return self.target_recipient.get_full_name()

	def get_seen(self):
		return self.seen





