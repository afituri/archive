# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from hnec.models import *
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta
import time

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
    c['department']=dept
    c['userid']=request.user.id
    return render_to_response('Departments.html',c)

@login_required(login_url='/')
def addDept(request):
    name = request.POST.get('Deptname','')
    dep = Department(name = name, status = True)
    dep.save()
    return  redirect('../Departments/')


@login_required(login_url='/')   
def editDepartment(request):
    id_department = request.POST['pk']
    name = request.POST['name']
    value = request.POST['value']  
    department = Department.objects.get(id=id_department)
    old = department.name
    department.name = value
    department.save()
    log = Log(id_user=request.user,action_type='edit',tabel='department',desc='edit department name :'+old+' = >'+department.name,tabel_id=department.id,value=department.name)
    log.save()
    return  redirect('../Departments/')

@login_required(login_url='/')
def addDepartment(request):
    c = {}
    c.update(csrf(request))
    objects=Section.objects.filter(Department_id=department_id,status=True)

    paginator=Paginator(objects,4)
    page = request.GET.get('page')
    try:
        section = paginator.page(page)
    except PageNotAnInteger :
        section = paginator.page(1)
    except EmptyPage:
        section = paginator.page(paginator.num_pages)
    c['sections']=section
    c['list']=objects
    c['userid']=request.user.id
    return render_to_response('addFolder.html',c)

@login_required(login_url='/') 
def department(request, department_id=0):
    c = {}
    c.update(csrf(request))
    if int(department_id)==0:
        return HttpResponseRedirect('/')
    if request.user.is_staff or int(department_id) == int(request.user.employee.department_id.id):
        q = request.GET.get('q')
        from_date = request.GET.get('start_date')
        to_date = request.GET.get('end_date')
        if q is not None:
            start_date=''
            end_date=''
            objects=Archive.objects.filter(department_id=department_id,status=True,ref_num__contains=q)
        elif from_date is not None and to_date is not None and from_date != '' and to_date != '':
            q=''
            start_date = datetime(year=int(from_date[0:4]), month=int(from_date[5:7]), day=int(from_date[8:10])).date()
            end_date = datetime(year=int(to_date[0:4]), month=int(to_date[5:7]), day=int(to_date[8:10])).date()
            objects=Archive.objects.filter(department_id=department_id,status=True,real_date__range=(start_date, end_date))
        else:
            start_date=''
            end_date=''
            q=''
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
        c['list']=Section.objects.filter(Department_id=department_id,status=True)
        c['dept_id']= department_id
        c['start_date']= start_date
        c['end_date']= end_date
        c['q']=q
        c['userid']=request.user.id
        c['departmentName']=Department.objects.get(id=department_id,status=True)
        return render_to_response('department.html',c)
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)

@login_required(login_url='/')
def addFolder(request, department_id=1):
    c = {}
    c.update(csrf(request))
    objects=Section.objects.filter(Department_id=department_id, status=True)
    paginator=Paginator(objects,4)
    page = request.GET.get('page')
    try:
        archive = paginator.page(page)
    except PageNotAnInteger :
        archive = paginator.page(1)
    except EmptyPage:
        archive = paginator.page(paginator.num_pages)
    # except paginator.page_range
    c['sections']=archive
    c['list']=objects
    c['dept_id']=department_id
    c['userid']=request.user.id
    c['departmentName']=Department.objects.get(id=department_id,status=True)
    return render_to_response('addFolder.html',c)

@login_required(login_url='/')
def editFolder(request):
    c = {}
    c.update(csrf(request))
    id_sect=request.POST['pk']
    name=request.POST['name']
    value=request.POST['value']  
    section = Section.objects.get(id=id_sect)
    old=section.name
    section.name = value
    section.save(update_fields=["name"])
    log = Log(id_user=request.user,action_type='edit',tabel='section',desc='edit section name :'+old+' = >'+section.name,tabel_id=section.id,value=section.name)   
    log.save()
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
            q = request.GET.get('q')
            from_date = request.GET.get('start_date')
            to_date = request.GET.get('end_date')
            if q is not None:
                start_date=''
                end_date=''
                objects=Archive.objects.filter(department_id=department_id,status=True,section_id=section_id,ref_num__contains=q)
            elif from_date is not None and to_date is not None and from_date != '' and to_date != '':
                q=''
                start_date = datetime(year=int(from_date[0:4]), month=int(from_date[5:7]), day=int(from_date[8:10])).date()
                end_date = datetime(year=int(to_date[0:4]), month=int(to_date[5:7]), day=int(to_date[8:10])).date()
                objects=Archive.objects.filter(section_id=section_id,department_id=department_id,status=True,real_date__range=(start_date, end_date))
            else:
                start_date=''
                end_date=''
                q=''
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
            c['dept_id']=department_id
            c['userid']=request.user.id
            c['list'] = Section.objects.filter(Department_id=department_id,status=True)
            c['q']=q
            c['start_date']= start_date
            c['end_date']= end_date
            c['departmentName']=Department.objects.get(id=department_id,status=True)
            return render_to_response('folder.html',c)
        else:
            return HttpResponseRedirect('/department/%s/%s' %(request.user.employee.department_id.id, sec_list[0]))    
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)

@login_required(login_url='/')
def addSection(request):
    c = {}
    c.update(csrf(request))
    sectionName = request.POST['name']
    department_id=Department.objects.get(id=request.POST['dept_id'])
    section = Section(name=sectionName,Department_id=department_id)
    section.save()
    log = Log(id_user=request.user,action_type='add',tabel='section',desc='add section '+sectionName,tabel_id=section.id,value=sectionName)
    log.save()
    return HttpResponseRedirect('/addFolder/%s/' %department_id.id,)

@login_required(login_url='/')
def addNewFolder(request):
    c = {}
    c.update(csrf(request))
    name = request.POST.get('Folder','')
    dept_id = request.POST.get('dept_id','')
    section = Section(name = name, status = True, Department_id = Department.objects.get(id=dept_id))
    section.save()
    log = Log(id_user=request.user,action_type='add',tabel='section',desc='add section '+name,tabel_id=section.id,value=name)
    log.save()
    return  redirect('../addFolder/%s/' %dept_id)

@login_required(login_url='/')
def deleteFolder(request, folder_id=0):
    c = {}
    c.update(csrf(request))
    flag = False
    if int(folder_id) != 0:
        archive = Archive.objects.filter(section_id=folder_id)
        for archive in archive:
            if archive.status == True:
                flag = True
                break

        if flag == False :
            section = Section.objects.get(id=folder_id)
            section.status = False
            section.save()
            log = Log(id_user=request.user,action_type='delete',tabel='section',desc='delete section '+section.name,tabel_id=section.id,value=section.name)
            log.save()
            # return HttpResponseRedirect('/addFolder/%s/' %section.Department_id.id,c,)
    flag=str(flag)+"$"+str(Section.objects.get(id=folder_id).Department_id.id)
    return HttpResponse(flag)

  
@login_required(login_url='/')
def deleteDepartment(request, department_id=0):
    if int(department_id) != 0:
        department = Department.objects.get(id=department_id)
        department.status = False
        department.save()
        log = Log(id_user=request.user,action_type='delete',tabel='department',desc='delete department '+department.name,tabel_id=department.id,value=department.name)
        log.save()
    return  HttpResponse(True)
