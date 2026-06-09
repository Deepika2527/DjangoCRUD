from django.shortcuts import render
import datetime

# Create your views here.
def test(request):
    mytime = datetime.datetime.now()
    my_dict = {
        'name' : 'Django Champs',
        'c' : "",
        'status' : "Currently im in django and completed react and everything",
        'marks' : [50,67,7,8,90],
        'duration' : 6,
        'mydate': mytime


            }
    return render(request, 'blogapp/test.html', my_dict)



def home(request):
    articles = [
        {
            "id": 1,
            "title": "Mastering Django Views",
            "content": "Django views are Python functions or classes that receive a web request and return a web response.",
            "viewdata": 15000,
            "category": "Programming"
        },
        {
            "id": 2,
            "title": "Python Performance Tips",
            "content": "Optimize your Python code by using built-in functions, list comprehensions, and proper data structures.",
            "viewdata": 42300,
            "category": "Python"
        },
        {
            "id": 4,
            "title": "Web Development in 2026",
            "content": "Discover the latest trends in web development, from server-side rendering to edge computing.",
            "viewdata": 8500,
            "category": "Web Tech"
        },
        {
            "id": 3,
            "title": "Web Development in 2026",
            "content": "Discover the latest trends in web development, from server-side rendering to edge computing.",
            "viewdata": 15000,
            "category": "Web Tech"
        }
    ]
    return render(request, 'blogapp/home.html', {'articles': articles})
