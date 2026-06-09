from django.urls import path
from .views import test,home


urlpatterns = [
    path("test/",test,name='test'),
    path("home/",home,name="home"),
]