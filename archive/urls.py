from django.conf.urls import patterns, include, url
from django.contrib import admin
from hnec.views import *

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', logIn),
    url(r'^department/$', department),
    url(r'^addArchive/$', addArchive),
    url(r'^editArchive/$', editArchive),
    url(r'^addFolder/$', addFolder),
    url(r'^auth/$', auth_view),
    url(r'^department/(?P<department_id>\d+)/$',department),
    url(r'^addDepartment/$', addDepartment),
    url(r'^cpanel/$', cpanel),
    url(r'^useres/$', users),
    url(r'^addUser/$', addUser),

)
