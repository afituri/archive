# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from hnec.models import *
from django.db.models import Count


@login_required(login_url='/')
def addFolder(request, department_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('addFolder.html',
        {'sections':Section.objects.filter(Department_id=department_id)},)


@login_required(login_url='/')
def addDepartment(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addDepartment.html',c)


@login_required(login_url='/')
def department(request, department_id=1):
    c = {}
    c.update(csrf(request))
    if request.user.is_staff or int(department_id) == int(request.user.employee.department_id.id):
        return render_to_response('department.html',{
                                    'department': Archive.objects.filter(department_id=department_id),
                                    'list':Section.objects.filter(Department_id=department_id),
                                    },    )
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)

@login_required(login_url='/')
def addDepartment(request):
    pass


@login_required(login_url='/')
def folder(request, department_id=1, section_id=1):
    c = {}
    c.update(csrf(request))
    sec_list = []
    if request.user.is_staff or int(department_id) == int(request.user.employee.department_id.id):
        for  sec_id in Section.objects.filter(Department_id=department_id):
            sec_list.append(sec_id.id)
        if request.user.is_staff or int(section_id) in sec_list:
            print 'it works so far'
            return render_to_response('folder.html',{
                                        'department': Archive.objects.filter(section_id=section_id),
                                        'list':Section.objects.filter(Department_id=department_id),
                                            },    )
        else:
            return HttpResponseRedirect('/department/%s/%s' %(request.user.employee.department_id.id, sec_list[0]))    
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)