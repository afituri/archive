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
def getArchive(request):
    c = {}
    c.update(csrf(request))
    archive = Section.objects.filter( Department_id=department_id,status=1)
    print "vbufbvriuvbnfsovj"
    print archive
    return archive


@login_required(login_url='/')
def addArchive(request, department_id=1):
    c = {}
    c.update(csrf(request))
    return render_to_response('addArchive.html',{
                                    'list':Section.objects.filter(Department_id=department_id),
                                    },    )