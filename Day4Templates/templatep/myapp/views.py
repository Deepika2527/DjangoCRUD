from django.shortcuts import render
import datetime

# Create your views here.

def wish(request):
    d_time = datetime.datetime.now()
    formatted_time  = d_time.strftime("%d-%m-%Y %H:%M:%S")
    print(formatted_time)
    name = "Anu"
    clas = "Django"
    mode = "online"

    mydict = {
        "Current_time" : formatted_time,
        "name": name,
        "class" : clas,
        "mode" : mode
    }




    return render(request, 'wish.html', mydict )

def wish1(request):
    mytime  = datetime.datetime.now()
    updateT = mytime.strftime("%d-%m-%Y %H:%M:%S")
    mes = "Hello all"
    h = int(mytime.strftime("%H"))
    print(h)

    if h<12:
        mes += "Good morning"
    elif h<16:
        mes += "Good Afternoon"
    elif h<20:
        mes += "Good Evening"
    else:
        mes = "Good Niught"

    mydic = {
        "time" : updateT,
        "message" : mes
    
    }
    return render(request, 'myap/wish1.html', mydic)


