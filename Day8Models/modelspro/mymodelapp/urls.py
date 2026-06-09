from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path('employee/',EmployeeView,name='EmployeeView'),
]