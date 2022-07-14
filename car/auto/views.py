from django.shortcuts import render
from django.http import HttpResponse
from .models import *

bmw = {"bmw": "cool car for best people"}
model_car = ["bmw", 'volvo', 'lada']


def base(request):
    return render(request, 'base.html', {"cars": model_car})


def all_cars(request):
    cars = Car.objects.all()
    manufacture = Manufacture.objects.all()
    context = {
        "cars": cars,
        "manufacture": manufacture,
    }
    return render(request, "all.html", context=context)


def car_lada(request):
    return render(request, "lada.html")


def car_bmw(request):
    return render(request, "bmw.html", bmw)


def car_volvo(request):
    return render(request, "volvo.html")
