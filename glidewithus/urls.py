from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'glidewithus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('glidewithus.landing.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    #url(r'^signup/', 'glidewithus.landing.views.signup', name="signup"),
    url(r'^profile', include('glidewithus.profiles.urls')),
    url(r'^logout', 'glidewithus.profiles.views.logout_view', name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'glidewithus.landing.views.home', name = 'home'),
    url(r'marketplace', 'glidewithus.marketplace.views.marketplace', name="marketplace"),
    url(r'message', 'glidewithus.marketplace.views.message', name="message"),
    url(r'settings', 'glidewithus.profiles.views.settings', name="settings"),

)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
