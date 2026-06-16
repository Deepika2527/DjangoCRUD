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
class EmployeeProject(models.Model):
    project_name = models.CharField(max_length=30)
    technlogies = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='project')

    def __str__(self):
        return self.project_name
class EmployeeSkills(models.Model):
    skills = models.CharField(max_length=50)
    employees = models.ManyToManyField(Employee,related_name='skills')

    def __str__(self):
        return self.skills
