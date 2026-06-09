from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age','date_joining','salary','work_mode']

admin.site.register(Employee,EmployeeAdmin)