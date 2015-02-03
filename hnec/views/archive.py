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
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
import os
import datetime
from django.shortcuts import render_to_response, RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# -*- coding: utf-8 -*-

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

@login_required(login_url='/')
def editArchive(request, archive_id=1):
    c = {}
    c.update(csrf(request))
    c['archive'] = Archive.objects.get(id=archive_id,status=1)
    if request.user.is_staff or int(c['archive'].department_id.id) == int(request.user.employee.department_id.id):
        c['list']=Section.objects.filter(Department_id=c['archive'].department_id.id,status=1)
        c['files']=Files.objects.filter(archive_id=archive_id,status=1)
        return render_to_response('editArchive.html',c)
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)
    


def addArchive(request, department_id=0):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('/cpanel/')
        else:
            return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)
    else:        
        return render_to_response('logIn.html',c)
    if int(department_id)!=0: 
        c['list']=Section.objects.filter(Department_id=department_id,status=True)
        c['dept_id']= department_id
        c['userid']=request.user.id
        c['departmentName']=Department.objects.get(id=department_id,status=True)
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
    archive = Archive.objects.get(id=id_u)
    print archive.id
    if name == 'name':
        old=archive.name
        archive.name=value
    elif name == 'real_date':
        old = archive.real_date
        archive.real_date = value
    elif name == 'ref_num':
        old = archive.ref_num
        archive.ref_num = value
    elif name == 'textarea':
        old = archive.text
        archive.text = value
    elif name == 'typesec':
        new = Section.objects.get(id=value)
        archive.section_id = new
        
    archive.save()

    # log = Log(id_user=request.user,action_type='edit',tabel='archive',desc='edit archive '+name+': '+old+' = > '+value,tabel_id=archive.id,value=value)
    # log.save()
    return HttpResponseRedirect('/',)

def insertArchive(request):
    files_name =[]
    i=0
    name = request.POST['name']
    ref_num = request.POST['ref_num']
    real_date = request.POST['real_date']
    section_id = Section.objects.get(id=request.POST['section_id'])
    text = request.POST['text']
    print real_date
    archive =Archive(name=name,real_date=real_date,section_id=section_id,department_id=section_id.Department_id,ref_num=ref_num,text=text)
    archive.save()
    log = Log(id_user=request.user,action_type='add',tabel='Archive',desc='add Archive '+name,tabel_id=archive.id,value=name)
    log.save()
    file_name= os.path.join("static","Files")
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+real_date[:4]
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+section_id.Department_id.name
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+name+"_"+str(archive.id)
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    for fil in request.POST.getlist('file_name[]'):
        files_name.append(fil)
    for files in request.FILES.getlist('file[]'):
        with open( file_name+"/"+files.name, 'wb+') as destination:
            for chunk in files.chunks():
                destination.write(chunk)
        if files_name[i] == '':
            files_name[i]=files.name
        f = Files(name = files_name[i] ,path =file_name+"/"+files.name,archive_id=archive )
        f.save()
        log = Log(id_user=request.user,action_type='add',tabel='Files',desc='add Files '+files_name[i],tabel_id=f.id,value=files_name[i])
        log.save()
        i=i+1
    return HttpResponseRedirect('/department/%s/' %section_id.Department_id.id)

@login_required(login_url='/')
def deleteFile(request,file_id=0):
    fil = Files.objects.get(id=file_id)
    fil.status = False
    fil.save()
    log = Log(id_user=request.user,action_type='delete',tabel='Files',desc='delete File '+fil.name,tabel_id=fil.id,value=fil.name)
    log.save()
    return HttpResponseRedirect('/',)

@login_required(login_url='/')
def deleteArchive(request,archive_id=0):
    archive = Archive.objects.get(id=archive_id)
    archive.status = False
    archive.save()
    log = Log(id_user=request.user,action_type='delete',tabel='archive',desc='delete archive '+archive.name,tabel_id=archive.id,value=archive.name)
    log.save()
    for fil in Files.objects.filter(archive_id=archive.id,status=True):
        fil.status = False
        fil.save()
        log = Log(id_user=request.user,action_type='delete',tabel='Files',desc='delete File '+fil.name,tabel_id=fil.id,value=fil.name)
        log.save()
    return HttpResponse(archive.department_id.id)

@login_required(login_url='/')
def addFile(request):
    files_name =[]
    i=0
    archive_id = request.POST['archive_id']
    archive =Archive.objects.get(id=archive_id)
    file_name= os.path.join("static","Files")
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+str(archive.real_date)[:4]
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+archive.department_id.name
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    file_name = file_name+"/"+archive.name+"_"+str(archive.id)
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    for fil in request.POST.getlist('file_name[]'):
        files_name.append(fil)
    print request.FILES.getlist('file[]')
    for files in request.FILES.getlist('file[]'):
        with open( file_name+"/"+files.name, 'wb+') as destination:
            for chunk in files.chunks():
                destination.write(chunk)
            if files_name[i] == '':
                files_name[i]=files.name
        f = Files(name = files_name[i] ,path =file_name+"/"+files.name,archive_id=archive )
        f.save()
        log = Log(id_user=request.user,action_type='add',tabel='Files',desc='add Files '+files_name[i],tabel_id=f.id,value=files_name[i])
        log.save()
        i=i+1
    return HttpResponseRedirect('/editArchive/%s/' %archive.id)
 
