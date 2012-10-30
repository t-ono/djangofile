# from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

    url(r'^polls/', include('polls.urls')),
#    url(r'^polls/$', 'index'),
#    url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),

)
