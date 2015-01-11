# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate
from hnec.models import *
from django.contrib import messages


def logIn(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('logIn.html',c)


@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


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
def cpanel(request):
    if request.user.is_staff:
        return render_to_response('cpanel.html',{'department':Department.objects.all()})
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)
