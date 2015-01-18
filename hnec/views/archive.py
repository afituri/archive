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
import os
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


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
def addArchive(request, department_id=0):
    c = {}
    c.update(csrf(request))
    if int(department_id)!=0: 
        c['list']=Section.objects.filter(Department_id=department_id)
        return render_to_response('addArchive.html',c)
    else:
        return HttpResponseRedirect('/',)

@login_required(login_url='/')
def getArchiveType(request, department_id=0):
    if int(department_id) != 0 :
        name=""
        ids=""
        for section in Section.objects.filter(Department_id=department_id,status=True):
            name=name+section.name+"$"
            ids=ids+str(section.id)+"$"
        return HttpResponse(name+ids)
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

def insertArchive(request):
    files_name =[]
    i=0
    name = request.POST['name']
    ref_num = request.POST['ref_num']
    real_date = request.POST['real_date']
    section_id = Section.objects.get(id=request.POST['section_id'])
    text = request.POST['text']
    archive =Archive(name=name,real_date=real_date,section_id=section_id,department_id=section_id.Department_id,ref_num=ref_num,text=text)
    archive.save()
    file_name= os.path.join(os.path.dirname(BASE_DIR), "static","Files")
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+real_date[:4]
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+section_id.Department_id.name
    print file_name
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+name+"_"+str(archive.id)
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    for fil in request.POST['file_name[]']:
        files_name.append(fil)
    for files in request.FILES.getlist('file[]'):
        with open( file_name+"/"+files.name, 'wb+') as destination:
            for chunk in files.chunks():
                destination.write(chunk)
        f = Files(name = files_name[i] ,path =file_name+"/"+files.name,archive_id=archive )
        f.save()
        i=i+1
 