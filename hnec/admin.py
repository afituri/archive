from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import Employee, Department

class EmployeeAdmin(admin.ModelAdmin):
	list_display=('user','department_id')
	class Meta:
		model = Employee

class DepartmentAdmin(admin.ModelAdmin):
	list_display=('name',)
	class Meta:
		model = Department

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)