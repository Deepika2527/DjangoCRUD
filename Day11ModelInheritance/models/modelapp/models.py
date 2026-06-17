from django.db import models

# Create your models here.
class Display(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        abstract = True
    def __str__(self):
        return self.name

class Teacher(Display):
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    phone_no = models.IntegerField()
class Student(Display):
    fee = models.DecimalField(max_digits=5,decimal_places=1)
    created_at = models.DateField()
    sub = models.CharField(max_length=10)

    def __str__(self):
        return f'studentname-{self.name},sub {self.sub}'

class ExamCenter(models.Model):
    center_name = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.center_name
class ExamRegistration(ExamCenter):
    fee = models.DecimalField(max_digits=5,decimal_places=1)
    student_name = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name


    
    

