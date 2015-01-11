# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect, RequestContext
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from django.contrib import messages

@login_required(login_url='/')
def cpanel(request):
    if request.user.is_staff:
        return render_to_response('cpanel.html',{'department':Department.objects.all()})
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)


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


def logIn(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('logIn.html',c)


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
def addArchive(request, department_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('addArchive.html',{
                                    'list':Section.objects.filter(Department_id=department_id),
                                    },    )


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


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user) #this login tell django that we want this user to login
        if request.user.is_staff:
            return HttpResponseRedirect('/cpanel/')
        else:
            return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)
    else:
        messages.warning(request, 'إسم المستخدم أو كلمة المرور غير صحيحة')
        return render_to_response('logIn.html', locals(), 
        context_instance=RequestContext(request))
        

@login_required(login_url='/')        
def sign(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('sign.html',c)

@login_required(login_url='/')
def users(request):
    if request.user.is_staff:
        c = {}
        c.update(csrf(request))
        c['users']=User.objects.filter(is_active=True)
        c['department']=Department.objects.filter(status=True)
        return render_to_response('users.html',c)
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)

@login_required(login_url='/')   
def addUser(request):
    username=request.POST['username']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    usertype=request.POST['usertype']
    user = User.objects.create_user(username,email,password)
    user.first_name=first_name
    user.last_name=last_name
    user.is_staff=True
    user.is_superuser=True
    user.save()
    if int(usertype) > 0: 
        user.is_staff=False
        user.is_superuser=False
        user.save()
        deptname=request.POST['deptname']
        department=Department.objects.get(id=deptname)
        employee=Employee(department_id=department,user=user)
        employee.save()
    return HttpResponseRedirect('/users/',)
    

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def addDepartment(request):
    pass
