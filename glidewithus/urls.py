from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'glidewithus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('glidewithus.landing.urls')),
    #url(r'^signup/', 'glidewithus.landing.views.signup', name="signup"),
    url(r'^profile', include('glidewithus.profiles.urls')),
    url(r'^logout', 'glidewithus.profiles.views.logout_view', name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'glidewithus.landing.views.home', name = 'home'),
    url(r'marketplace', 'glidewithus.marketplace.views.marketplace', name="marketplace")
)
