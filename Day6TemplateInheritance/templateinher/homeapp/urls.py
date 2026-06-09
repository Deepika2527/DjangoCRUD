from django.urls import path
from .views import home,course


urlpatterns=[
    path("home/",home,name="home"),
    path("courses/",course,name="course"),
]