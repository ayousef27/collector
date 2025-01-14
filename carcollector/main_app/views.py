from django.shortcuts import render, redirect
from .models import Car
from .forms import OilForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    oil_form = OilForm()
    return render(request, 'cars/details.html', {'car': car, 'oil_form': oil_form})

def add_oil(request, car_id):
  
  form = OilForm(request.POST)
  
  if form.is_valid():
    
    new_oil = form.save(commit=False)
    new_oil.car_id = car_id
    new_oil.save()
  return redirect('details', car_id=car_id)
    

class CarCreate(CreateView):
  model = Car
  fields = ['name', 'model', 'color', 'production']
#   success_url = '/cars/'


class CarUpdate(UpdateView):
  model = Car
  
  fields = ['model', 'color', 'production']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'