from django.shortcuts import render
from .models import Employee,EmployeeProfile

# Create your views here.
def display(request):
    employee = Employee.objects.all()
    context = {'employees': employee}
    return render(request,'employee.html',context)
