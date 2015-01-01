from django.db import models
from django.contrib.auth.models import User 
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
 


def upload_file(instance,name):
    return os.path.join(os.path.dirname(BASE_DIR),"learn_django", "static")+"/up/"+name

class Department(models.Model):
    name = models.CharField(max_length = 50)
    modify_date = models.DateTimeField(auto_now=True,auto_now_add=False)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    status = models.BoolenField(default=True)

    def __unicode__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length = 50)
    modify_date = models.DateTimeField(auto_now=True,auto_now_add=False)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    Department_id = models.ForeignKey(Department)
    status = models.BoolenField(default=True)

    def __unicode__(self):
        return self.name


class Archive(models.Model):
    name = models.CharField(max_length = 50)
    modify_date = models.DateTimeField(auto_now=True,auto_now_add=False)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    real_date = models.DateTimeField()
    section_id = models.ForeignKey(Section)
    department_id = models.ForeignKey(Department)
    ref_num = models.CharField(max_length = 50)
    text = models.CharField(max_length = 500)
    status = models.BoolenField(default=True)

    def __unicode__(self):
        return self.name


class Files(models.Model):
    name = models.CharField(max_length = 50)
    path = models.FileField(upload_to=upload_file)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    archive_id =  models.ForeignKey(Archive)
    status = models.BoolenField(default=True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User)
    department_id = models.ForeignKey(Department)

    def __unicode__(self):
        return self.department_id


class Log(models.Model):
    id_user = models.ForeignKey(User)
    action_type = models.CharField(max_length = 50)
    tabel = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 50)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    tabel_id = models.IntegerField()
    value = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.action_type

