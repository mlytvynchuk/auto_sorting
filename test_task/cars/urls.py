from django.urls import path, include
from .views import car_list

urlpatterns = [
    path('',car_list,name='cars_list'),

]
