from django.conf.urls import patterns, include, url
from django.contrib import admin
from hnec.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archive.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^department/$', department),
)
