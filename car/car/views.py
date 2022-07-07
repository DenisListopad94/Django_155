from django.http import HttpResponse
from django.shortcuts import render


def car_main(request):
    return HttpResponse("<H1>Hello Django</H1>")


