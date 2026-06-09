from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_joining = models.DateField()
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    work_mode = models.BooleanField()
    


    def __str__(self):
        return self.name



    

