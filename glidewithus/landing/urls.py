from django.conf.urls import patterns, url
import views

urlpatterns = patterns('', 
	url(r'^$', views.landing, name='landing'),
	url(r'^signup/', views.signup, name="signup"),
	url(r'^login/', views.login, name="login")
	#url(r'^signin/', views.signin, name='signin'),
)

