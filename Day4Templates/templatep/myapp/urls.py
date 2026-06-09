from django.urls import path
from .views import wish, wish1


urlpatterns = [

  path("wish/",wish,name="wish"),
  path("wish1/", wish1, name="wish1"),

]