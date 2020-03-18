from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero

# class Superhero:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, power, description, age):
#     self.name = name
#     self.power = power
#     self.description = description
#     self.age = age


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def superheroes_index(request):
    superheroes = Superhero.objects.all()
    return render(request, 'superheroes/index.html', {'superheroes': superheroes})