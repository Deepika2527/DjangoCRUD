from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.name
    
class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.employee.name
