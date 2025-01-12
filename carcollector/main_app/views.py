from django.shortcuts import render
from .models import Car
# Create your views here.
from django.http import HttpResponse






# Define the home view
def home(request):
    return HttpResponse('<h1>Hello car </h1>')

def about(request):
    
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', {'car': car})