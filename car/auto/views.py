from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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


def add_comment_form(request):
    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
            CommenModel.objects.create(**form.cleaned_data)
            return redirect("/auto/all/")
    else:
        form = Comment()
    return render(request,'comment.html',{'form':form})

def car_form(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auto/all/")
    else:
        form = CarForm()
    return render(request,'car_form.html',{'form':form})

