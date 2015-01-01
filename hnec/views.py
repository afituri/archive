from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('base.html',c)

def department(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('department.html',c)

def auth_view(request):
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=email, password=password)
    if user is not None:
        auth.login(request,user) #this login tell django that we want this user to login
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/invaild_login/')

@login_required(login_url='/')
def loggedin(request):
    print("it worked")
    return render_to_response('loggedin.html',
        {'full_name': request.user.last_name}
        )

def invaild_login(request):
    return render_to_response('invaild_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
