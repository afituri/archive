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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def logIn(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        if request.user.is_staff:
            return HttpResponseRedirect('/cpanel/')
        else:
            return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)
    else:        
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

        objects=c['users']
        paginator=Paginator(objects,10)
        page = request.GET.get('page')
        try:
            USERS = paginator.page(page)
        except PageNotAnInteger :
            USERS = paginator.page(1)
        except EmptyPage:
            USERS = paginator.page(paginator.num_pages)
        c['users']=USERS
        # except paginator.page_range
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
    log = Log(id_user=request.user,action_type='add',tabel='user',desc='add user '+username,tabel_id=user.id,value=username)
    log.save()
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
def editUser(request,user_id=1):
    if request.user.is_staff:
        c = {}
        c.update(csrf(request))
        c['user']=User.objects.get(id=user_id,is_active=True)
        return render_to_response('editUser.html',c)
    else:
       return HttpResponseRedirect('/',) 

@login_required(login_url='/')
def edit(request):
    id_u=request.POST['pk']
    name=request.POST['name']
    value=request.POST['value']
    user=User.objects.get(id=id_u)
    if name == 'username':
        old=user.username
        user.username=value
    elif name == 'first_name':
        old = user.first_name
        user.first_name = value
    elif name == 'last_name':
        old = user.last_name
        user.last_name = value
    elif name == 'email':
        old = user.email
        user.email = value
    user.save()
    log = Log(id_user=request.user,action_type='edit',tabel='user',desc='edit user '+name+': '+old+' = > '+value,tabel_id=user.id,value=value)
    log.save()
    return HttpResponseRedirect('/',)



@login_required(login_url='/')
def cpanel(request):
    if request.user.is_staff:
        return render_to_response('cpanel.html',{'department':Department.objects.all()})
    else:
        return HttpResponseRedirect('/department/%s/' %request.user.employee.department_id.id)

# not working
# def checkUsername(request):
#     # username=request.POST['username']
#     # user=User.objects.get(username=username)
#     print "asdfasfasfaf"
#     return True
#     # print username
#     # if user is not None:
#     #     return False
#     # else:
#     #     return True
