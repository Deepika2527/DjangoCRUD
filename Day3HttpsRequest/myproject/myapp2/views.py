from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def greeting(request):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>The current Time is: " +formatted_time+ "</h1>")
