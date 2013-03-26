from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LRC.views.home', name='home'),
    # url(r'^LRC/', include('LRC.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^member/', include('members.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^membership/', include('membership.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
