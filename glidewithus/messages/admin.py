from django.contrib import admin
from models import message

# Register your models here.

class messsagesAdmin(admin.ModelAdmin):
	list_display = ['sender', 'reciever', 'seen', 'time_started']


admin.site.register(messagesAdmin, messages)
