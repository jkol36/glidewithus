from django.contrib import admin
from models import requested_invites

# Register your models here.

class requested_invitesAdmin(admin.ModelAdmin):
	fields = ['email', 'mission_statement']
	list_display = ['email', 'mission_statement']

admin.site.register(requested_invites, requested_invitesAdmin)
