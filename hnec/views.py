from django.shortcuts import render
from django.shortcuts import render_to_response, render, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('base.html',c)

# def addFolder(request):
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('base.html',c)

def home(request):
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

def department(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('department.html',c)

