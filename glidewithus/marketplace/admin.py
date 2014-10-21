from django.contrib import admin
from models import *

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
	fields = ['interest', 'company', 'profession', 'keyword']
	list_display = ['interest', 'company', 'profession', 'keyword']

admin.site.register(Search, SearchAdmin)
