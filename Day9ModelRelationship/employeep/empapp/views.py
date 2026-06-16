from django.shortcuts import render
from .models import Employee,EmployeeProfile,EmployeeProject,EmployeeSkills

# Create your views here.
def display(request):
    employee = Employee.objects.all()
    context = {'employees': employee}
    return render(request,'employee.html',context)
def EmployeeProjectView(request):
    employeep = Employee.objects.all()
    emp_pro = {'projects':employeep}
    return render(request,'employee_pro.html',emp_pro)
def EmployeeSkillView(request):
    emp_skill = Employee.objects.all()
    emp_skills = {'empskills':emp_skill}
    return render(request,'employee_skill.html',emp_skills)

