from django.contrib import admin
from models import meetuprequest

# Register your models here.

class meetupAdmin(admin.ModelAdmin):
	field_set = ['seen', 'target_sender', 'target_recipient', 'start_time', 'date', 'message', 'response']
	list_display= ['target_recipient', 'target_sender', 'start_time', 'date', 'message', 'response']
admin.site.register(meetuprequest, meetupAdmin)
