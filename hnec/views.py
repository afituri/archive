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

# Create your views here.

def cpanel(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('cpanel.html',c)

def addFolder(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addFolder.html',c)

def addDepartment(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addDepartment.html',c)

def logIn(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('logIn.html',c)

def editArchive(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('editArchive.html',c)

def addArchive(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addArchive.html',c)


@login_required(login_url='/')
def department(request, department_id=1):
    c = {}
    c.update(csrf(request))
    print Archive.objects.filter(department_id=department_id)
    return render_to_response('department.html',{
                                'department': Archive.objects.filter(department_id=department_id),
                                'list':Section.objects.filter(Department_id=department_id),
                                },    )


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

#@staff_member_required for cpanel

