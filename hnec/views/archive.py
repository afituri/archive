# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from hnec.models import *


@login_required(login_url='/')
def editArchive(request, archive_id=1):
    c = {}
    c.update(csrf(request))
    archive = Archive.objects.get(id=archive_id,status=1)
    return render_to_response('editArchive.html',{
                                    'archive':archive,
                                    'list':Section.objects.filter(Department_id=archive.department_id.id,status=1),
                                    'files':Files.objects.filter(archive_id=archive_id,status=1),
                                    },    )


@login_required(login_url='/')
def getArchive(request):
    c = {}
    c.update(csrf(request))
    archive = Section.objects.filter( Department_id=department_id,status=True)
    print "vbufbvriuvbnfsovj"
    print archive
    return archive


@login_required(login_url='/')
def addArchive(request, department_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('addArchive.html',{
                                    'list':Section.objects.filter(Department_id=department_id),
                                    },    )

@login_required(login_url='/')
def getArchiveType(request, department_id=0):
    if int(department_id) != 0 :
        section = Section.objects.filter(Department_id=department_id,status=True)
        print section
        return HttpResponse(section)
    else:
        print "False False hbfourebfrefhbrpihnpi;"
        return HttpResponse(False)

@login_required(login_url='/')
def editArchiveEditable(request):

    id_u = request.POST['pk']
    name = request.POST['name']
    value = request.POST['value']

    user = User.objects.get(id=id_u)

    if name == 'username':
        old=user.username
        user.username=value
    elif name == 'first_name':
        old = user.first_name
        user.first_name = value
    elif name == 'last_name':
        old = user.last_name
        user.last_name = value
    elif name == 'email':
        old = user.email
        user.email = value
    user.save()
    log = Log(id_user=request.user,action_type='edit',tabel='user',desc='edit user '+name+': '+old+' = > '+value,tabel_id=user.id,value=value)
    log.save()
    return HttpResponseRedirect('/',)