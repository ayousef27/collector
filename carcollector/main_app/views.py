from django.shortcuts import render, redirect
from .models import Car, Medal
from .forms import OilForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.






# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    oil_form = OilForm()
    medals_car_doesnt_have = Medal.objects.exclude(id__in = car.medals.all().values_list('id'))
    return render(request, 'cars/details.html', {'car': car, 'oil_form': oil_form, 'medals': medals_car_doesnt_have})

def add_oil(request, car_id):
  
  form = OilForm(request.POST)
  
  if form.is_valid():
    
    new_oil = form.save(commit=False)
    new_oil.car_id = car_id
    new_oil.save()
  return redirect('details', car_id=car_id)

def assoc_medal(request, car_id, medal_id):
    Car.objects.get(id=car_id).medals.add(medal_id)
    return redirect('details', car_id = car_id)

def unassoc_medal(request, car_id, medal_id):
    Car.objects.get(id=car_id).medals.remove(medal_id)
    return redirect('details', car_id = car_id)
    

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

class MedalList(ListView):
    model = Medal

class MedalDetail(DetailView):
    model = Medal

class MedalCreate(CreateView):
    model = Medal
    fields = '__all__'

class MedalUpdate(UpdateView):
    model = Medal
    fields = ['name', 'color']

class MedalDelete(DeleteView):
    model = Medal
    success_url = '/medals/'