from django.conf.urls import patterns, include, url
from django.contrib import admin
from hnec.views import *

urlpatterns = patterns('',

	url(r'^$', home),
    url(r'^department/$', department),
    url(r'^addArchive/$', addArchive),
    url(r'^editArchive/$', editArchive),
    url(r'^addFolder/$', addFolder),

)
