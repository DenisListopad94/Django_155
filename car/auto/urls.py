from django.urls import path
from .views import *

urlpatterns = [
    path('lada/',car_lada,name = 'lada'),
    path('bmw/', car_bmw,name = 'bmw'),
    path('all/', all_cars,name = 'all'),
    path('volvo/',car_volvo,name='volvo'),
    path('base/',base)
]
