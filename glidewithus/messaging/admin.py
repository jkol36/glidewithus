from django.contrib import admin
from models import message

# Register your models here.

class messagesAdmin(admin.ModelAdmin):
	list_display = ['sender', 'recipient', 'seen', 'sent_at']


admin.site.register(message, messagesAdmin)
