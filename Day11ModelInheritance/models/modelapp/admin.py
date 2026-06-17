from django.contrib import admin
from .models import Teacher,Student,ExamCenter,ExamRegistration

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','age','created_at','salary','phone_no']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','fee','created_at']

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','center_name','city','state']

@admin.register(ExamRegistration)
class ExamRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','fee','center_name']