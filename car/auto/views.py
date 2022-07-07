from django.shortcuts import render
from django.http import HttpResponse

bmw = {"bmw":"cool car for best people"}
model_car = ["bmw",'volvo','lada']

def base(request):
    return render(request,'base.html',{"cars":model_car})

def car_lada(request):
    return render(request, "lada.html")

def car_bmw(request):
    return render(request, "bmw.html",bmw)

def car_volvo(request):
    return render(request, "volvo.html")