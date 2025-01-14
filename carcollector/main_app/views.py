from django.shortcuts import render, redirect
from .models import Car, Medal
from .forms import OilForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.






# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    oil_form = OilForm()
    medals_car_doesnt_have = Medal.objects.exclude(id__in = car.medals.all().values_list('id'))
    return render(request, 'cars/details.html', {'car': car, 'oil_form': oil_form, 'medals': medals_car_doesnt_have})

@login_required
def add_oil(request, car_id):
  
  form = OilForm(request.POST)
  
  if form.is_valid():
    
    new_oil = form.save(commit=False)
    new_oil.car_id = car_id
    new_oil.save()
  return redirect('details', car_id=car_id)

@login_required
def assoc_medal(request, car_id, medal_id):
    Car.objects.get(id=car_id).medals.add(medal_id)
    return redirect('details', car_id = car_id)

@login_required
def unassoc_medal(request, car_id, medal_id):
    Car.objects.get(id=car_id).medals.remove(medal_id)
    return redirect('details', car_id = car_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid Signup- please try again later.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    

class CarCreate(LoginRequiredMixin,CreateView):
  model = Car
  fields = ['name', 'model', 'color', 'production']
  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
#   success_url = '/cars/'




class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  
  fields = ['model', 'color', 'production']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

class MedalList(LoginRequiredMixin, ListView):
    model = Medal

class MedalDetail(LoginRequiredMixin, DetailView):
    model = Medal

class MedalCreate(LoginRequiredMixin, CreateView):
    model = Medal
    fields = '__all__'

class MedalUpdate(LoginRequiredMixin, UpdateView):
    model = Medal
    fields = ['name', 'color']

class MedalDelete(LoginRequiredMixin, DeleteView):
    model = Medal
    success_url = '/medals/'