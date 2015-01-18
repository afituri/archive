# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from hnec.models import *
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required(login_url='/')
def addFolder(request, department_id=1):
    c = {}
    c.update(csrf(request))
    c['sections']=Section.objects.filter(Department_id=department_id)
    c['list']=Section.objects.filter(Department_id=department_id)
    return render_to_response('addFolder.html',c)

@login_required(login_url='/')
def editFolder(request):
    c = {}
    c.update(csrf(request))
    id_sect=request.POST['pk']
    name=request.POST['name']
    value=request.POST['value']  
    section = Section.objects.get(id=id_sect)
    section.name = value
    section.save(update_fields=["name"])
    return render_to_response('addFolder.html',c)

@login_required(login_url='/')
def Departments(request):
        c = {}
        c.update(csrf(request))
        objects=Department.objects.filter(status=True)
        paginator=Paginator(objects,10)
        page = request.GET.get('page')
        try:
            dept = paginator.page(page)
        except PageNotAnInteger :
            dept = paginator.page(1)
        except EmptyPage:
            dept = paginator.page(paginator.num_pages)
        # except paginator.page_range
        c['department']=dept
        return render_to_response('Departments.html',c)

@login_required(login_url='/')   
def addDept(request):
    name = request.POST.get('Deptname','')
    dep = Department(name = name, status = True)
    dep.save()
    return  redirect('../Departments/')





@login_required(login_url='/')
def deletFolder(request):
    pass


def addDepartment(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addFolder.html',
        {'sections':Section.objects.filter(Department_id=department_id)},)



@login_required(login_url='/')
def department(request, department_id=0):
    c = {}
    c.update(csrf(request))
    if int(department_id)==0:
        return HttpResponseRedirect('/')
    if request.user.is_staff or int(department_id) == int(request.user.employee.department_id.id):
        objects=Archive.objects.filter(department_id=department_id,status=True)
        paginator=Paginator(objects,4)
        page = request.GET.get('page')
        try:
            archive = paginator.page(page)
        except PageNotAnInteger :
            archive = paginator.page(1)
        except EmptyPage:
            archive = paginator.page(paginator.num_pages)
        # except paginator.page_range
        c['archive']=archive
        c['list']=Section.objects.filter(Department_id=department_id)
        return render_to_response('department.html',c)
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
            objects=Archive.objects.filter(department_id=department_id,status=True,section_id=section_id)
            paginator=Paginator(objects,4)
            page = request.GET.get('page')
            try:
                archive = paginator.page(page)
            except PageNotAnInteger :
                archive = paginator.page(1)
            except EmptyPage:
                archive = paginator.page(paginator.num_pages)
            c['archive'] = archive
            c['list'] = Section.objects.filter(Department_id=department_id)
            return render_to_response('folder.html',c)
        else:
            return HttpResponseRedirect('/department/%s/%s' %(request.user.employee.department_id.id, sec_list[0]))    
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)


        