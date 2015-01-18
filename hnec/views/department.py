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
    c['departmentId']= department_id
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
        c['department']=archive
        c['list']=Section.objects.filter(Department_id=department_id)
        c['dept_id']= request.user.employee.department_id.id
        return render_to_response('department.html',c)
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)

@login_required(login_url='/')
def addFolder(request, department_id=1):
    c = {}
    c.update(csrf(request))
    c['sections']=Section.objects.filter(Department_id=department_id, status=True)
    c['list']=Section.objects.filter(Department_id=department_id, status=True)
    c['dept_id']=request.user.employee.department_id.id
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

# dispalys section
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

@login_required(login_url='/')   
def addSection(request):
    sectionName = request.POST['name']
    department_id=Department.objects.get(id=request.POST['departmentId'])
    section = Section(name=sectionName,Department_id=department_id)

    section.save()
    
    log = Log(id_user=request.user,action_type='add',tabel='section',desc='add section '+sectionName,tabel_id=section.id,value=sectionName)
    log.save()
   
    return HttpResponseRedirect('/users/',)
@login_required(login_url='/')
def addNewFolder(request):
    name = request.POST.get('Folder','')
    dept_id = request.POST.get('dept_id','')
    section = Section(name = name, status = True, Department_id = Department.objects.get(id=dept_id))
    section.save()
    return  redirect('../addFolder/%s/' %dept_id)


@login_required(login_url='/')
def deleteFolder(request, folder_id=0):
    print 'this sucks'
    if int(folder_id) != 0:
        section = Section.objects.get(id=folder_id)
        section.status = False
        section.save()
        print 'this sucks again'
    return HttpResponseRedirect('/',)