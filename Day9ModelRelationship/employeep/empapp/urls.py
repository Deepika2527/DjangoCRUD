from django.urls import path
from .views import display,EmployeeProjectView,EmployeeSkillView

urlpatterns  = [
    path('disp/',display,name='display'),
    path('project/',EmployeeProjectView,name='EmployeeProjectView'),
    path('skills/',EmployeeSkillView,name='EmployeeSkillView'),
]