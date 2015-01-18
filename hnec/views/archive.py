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

    archive.save()

    log = Log(id_user=request.user,action_type='edit',tabel='archive',desc='edit archive '+name+': '+old+' = > '+value,tabel_id=archive.id,value=value)
    log.save()
    # return HttpResponseRedirect('/',)
    return True