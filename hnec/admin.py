from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import *

class FilesAdmin(admin.ModelAdmin):
	list_display=('name',)
	class Meta:
		model = Files

class EmployeeAdmin(admin.ModelAdmin):
	list_display=('user','department_id')
	class Meta:
		model = Employee

class DepartmentAdmin(admin.ModelAdmin):
	list_display=('name',)
	class Meta:
		model = Department

class SectionAdmin(admin.ModelAdmin):
	list_display=('name',)
	class Meta:
		model = Section

class ArchiveAdmin(admin.ModelAdmin):
	list_display=('name',)
	class Meta:
		model = Archive

admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Files, FilesAdmin)