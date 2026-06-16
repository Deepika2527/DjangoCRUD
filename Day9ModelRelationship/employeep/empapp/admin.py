from django.contrib import admin
from .models import Employee,EmployeeProfile,EmployeeProject,EmployeeSkills

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','emp_id']

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['employee','phone','adress','email']


@admin.register(EmployeeProject)
class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ['id','employee','project_name','technlogies']
admin.site.register(EmployeeSkills)
