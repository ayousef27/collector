from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, model, color, production):
    self.name = name
    self.model = model
    self.color = color
    self.production = production

cars = [
  Car('camry', 'fjdnb', 'red', 2017),
  Car('echo', 'jkgnj', 'green', 2015),
  Car('bugati', 'ruigber', 'yellow ', 2014),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello car </h1>')

def about(request):
    
    return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })