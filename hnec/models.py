from django.db import models
from django.contrib.auth.models import User 

class Department(models.Model):
    name = models.CharField(max_length = 50)
    modify_date = models.DateTimeField(auto_now=True,auto_now_add=False)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length = 50)
    modify_date = models.DateTimeField(auto_now=True,auto_now_add=False)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    Department_id = models.ForeignKey(Department)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Archive(models.Model):
    name = models.CharField(max_length = 50)
    modify_date = models.DateTimeField(auto_now=True,auto_now_add=False)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    real_date = models.DateField()
    section_id = models.ForeignKey(Section)
    department_id = models.ForeignKey(Department)
    ref_num = models.CharField(max_length = 50)
    text = models.CharField(max_length = 500)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Files(models.Model):
    name = models.CharField(max_length = 50)
    path = models.CharField(max_length = 300)
    create_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    archive_id =  models.ForeignKey(Archive)
    status = models.BooleanField(default =True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User)
    department_id = models.ForeignKey(Department)


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
