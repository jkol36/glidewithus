from django.contrib import admin
from locations.models import City
from models import GlideProfile, Interest, Company, Proffession
from sorl.thumbnail.admin import AdminImageMixin





class GlideProfileAdmin(AdminImageMixin, admin.ModelAdmin):
	fields = ['mission_statement', 'profile',  'state', 'country', 'age', 'profile_pic' ]
	list_display  = ['mission_statement', 'profile', 'profile_pic', 'city', 'age','country', 'state','has_profile_pic','isfacebook_user', 'istwitter_user', 'why_awesome', 'traveler_pitch']
class CityAdmin(admin.ModelAdmin):
	fields = ['name', 'country', 'state', 'has_local', 'total_locals']
	list_display = ['name', 'country', 'has_local', 'total_locals']

class InterestAdmin(admin.ModelAdmin):
	fields = ['name', 'user']
	list_display = ['name']

class CompanyAdmin(admin.ModelAdmin):
	fields = ['name', 'user']
	list_display = ['name']

class ProfessionAdmin(admin.ModelAdmin):
	fields = ['name', 'user']
	list_display = ['name']



admin.site.register(Proffession, ProfessionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(GlideProfile, GlideProfileAdmin)
admin.site.register(City, CityAdmin)