from django.conf.urls import patterns, url, include
import views


urlpatterns = patterns('', 
	url(r'^', views.profile, name='profile'),
	url(r'^removeinterest', views.removeinterest, name="removeinterest"),
	)