from django.shortcuts import render

import datetime

# Create your views here.

def greet(request):
    d = datetime.datetime.now()
    formattedD = d.strftime("%d-%m-%Y %H:%M:%S")

    name = "Anu"
    exp = 3
    role = "FullStackDeveloper"
    salary = 90000

    mydict ={
        "name" : name,
        "role" : role,
        "expr" : exp,
        "salary" : salary,
        "doj" : formattedD
    }


    return render(request, 'greet.html', mydict)


