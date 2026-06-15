from django.urls import path
from .views import display

urlpatterns  = [
    path('disp/',display,name='display'),
]