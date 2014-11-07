from django.db import models
from glidewithus.profiles.models import GlideProfile


# Create your models here.

class conversation(models.Model):
	time_started = models.DateTimeField(auto_now_add=True)

