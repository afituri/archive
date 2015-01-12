from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'hnec.views.users.logIn'),
    url(r'^department/$', 'hnec.views.department.department'),
    url(r'^addArchive/$', 'hnec.views.archive.addArchive'),
    url(r'^editArchive/(?P<archive_id>\d+)/$', 'hnec.views.archive.editArchive'),
    url(r'^addFolder/$', 'hnec.views.department.addFolder'),
    url(r'^auth/$', 'hnec.views.users.auth_view'),
    url(r'^department/(?P<department_id>\d+)/$','hnec.views.department.department'),
    url(r'^addDepartment/$', 'hnec.views.department.addDepartment'),
    url(r'^cpanel/$', 'hnec.views.users.cpanel'),
    url(r'^users/$', 'hnec.views.users.users'),
    url(r'^addUser/$', 'hnec.views.users.addUser'),
    url(r'^logout/$', 'hnec.views.users.logout'),
    url(r'^users/editUser/(?P<user_id>\d+)/$', 'hnec.views.users.editUser'),
    # url(r'^/username/$', 'hnec.views.users.checkUsername'),not working
    url(r'^users/edit/$', 'hnec.views.users.edit'),
)
