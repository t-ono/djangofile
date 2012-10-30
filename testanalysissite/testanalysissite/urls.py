# from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testanalysissite.views.home', name='home'),
    # url(r'^testanalysissite/', include('testanalysissite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
	url(r'^analysis/$','analysis.views.index'),
	url(r'^analysis/selectsub/$', 'analysis.views.selectsub'),
	url(r'^analysis/(?P<sub_id>\d+)$', 'analysis.views.detail'),
	url(r'^analysis/(?P<sub_id>\d+)/selectexp/$', 'analysis.views.selectexp'),
	url(r'^analysis/(?P<sub_id>\d+)/(?P<exp_id>\d+)/dataview/$','analysis.views.dataview'),
	url(r'^analysis/(?P<sub_id>\d+)/(?P<exp_id>\d+)/dataview/rawsignal.png$','analysis.views.plotrawsignal'),
	url(r'^analysis/(?P<sub_id>\d+)/(?P<exp_id>\d+)/dataview/tfmap.png$','analysis.views.tfmap'),
	url(r'^analysis/(?P<sub_id>\d+)/(?P<exp_id>\d+)/dataview/tpplot.png$','analysis.views.tpplot'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
