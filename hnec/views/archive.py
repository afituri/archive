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
    c['list']=Section.objects.filter(Department_id=c['archive'] .department_id.id,status=1)
    c['files']=Files.objects.filter(archive_id=archive_id,status=1)
    return render_to_response('editArchive.html',c)


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
        c['list']=Section.objects.filter(Department_id=department_id,status=True)
        c['dept_id']= department_id
        c['userid']=request.user.id
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


# @login_required(login_url='/')
# def getArchiveType(request, department_id=0):
#     if int(department_id) != 0 :
#         section = Section.objects.filter(Department_id=department_id,status=True)
#         print section
#         model_to_dict(section)
#         # return HttpResponse(section)
#         return section
#     else:
#         print "False False hbfourebfrefhbrpihnpi;"
#         return HttpResponse(False)#send string only


@login_required(login_url='/')
def editArchiveEditable(request):
    id_u = request.POST['pk']
    name = request.POST['name']
    value = request.POST['value']
    archive = Archive.objects.get(id=id_u)
    print value
    if name == 'name':
        old=archive.name
        archive.name=value
    elif name == 'real_date':
        old = archive.real_date
        archive.real_date = value
    elif name == 'ref_num':
        old = archive.ref_num
        archive.ref_num = value
    elif name == 'text':
        old = archive.text
        archive.text = value
    elif name == 'type':
        old = Section.objects.get(id=archive.section_id.id)
        new=Section.objects.get(id=int(value))
        archive.section_id = int(value)
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
    archive =Archive(name=name,real_date=real_date,section_id=section_id,department_id=section_id.Department_id,ref_num=ref_num,text=text)
    archive.save()
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
        f = Files(name = files_name[i] ,path =file_name+"/"+files.name,archive_id=archive )
        f.save()
        i=i+1
    return HttpResponseRedirect('/department/%s/' %section_id.Department_id.id)
 
