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
    url(r'^addFolder/(?P<department_id>\d+)/$', 'hnec.views.department.addFolder'),
    url(r'^auth/$', 'hnec.views.users.auth_view'),
    url(r'^department/(?P<department_id>\d+)/$','hnec.views.department.department'),
    url(r'^addDepartment/$', 'hnec.views.department.addDepartment'),
    url(r'^cpanel/$', 'hnec.views.users.cpanel'),
    url(r'^users/$', 'hnec.views.users.users'),
    url(r'^addUser/$', 'hnec.views.users.addUser'),
    url(r'^Departments/$', 'hnec.views.department.Departments'),
    url(r'^addDept/$', 'hnec.views.department.addDept'),
    url(r'^logout/$', 'hnec.views.users.logout'),
    url(r'^users/editUser/(?P<user_id>\d+)/$', 'hnec.views.users.editUser'),
    url(r'^/username/$', 'hnec.views.users.checkUsername'),
    url(r'^users/edit/$', 'hnec.views.users.edit'),
    url(r'^users/deleteUser/(?P<user_id>\d+)/$', 'hnec.views.users.deleteUser'),
    url(r'^getSection/(?P<department_id>\d+)/$','hnec.views.archive.getArchive'),
    url(r'^department/(?P<department_id>\d+)/(?P<section_id>\d+)/$', 'hnec.views.department.folder'),
    url(r'^getArchiveType/(?P<department_id>\d+)/$','hnec.views.archive.getArchiveType'),
    url(r'^editFolder/$', 'hnec.views.department.editFolder'),
    url(r'^deleteFolder/(?P<folder_id>\d+)/$', 'hnec.views.department.deleteFolder'),
    url(r'^addNewFolder/$', 'hnec.views.department.addNewFolder'),
    
)
