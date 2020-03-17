from django.shortcuts import render
from django.http import HttpResponse

class Superhero:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, power, description, age):
    self.name = name
    self.power = power
    self.description = description
    self.age = age

superheroes = [
  Superhero('Wonder Woman', 'Amazon', 'princess of themyscira', 3),
  Superhero('Iron Man', 'super smart', 'playboy millionaire philanthropist', 0),
  Superhero('Captain Marvel', 'OP', 'inhaled inifinity stone power', 4)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def superheroes_index(request):
    return render(request, 'superheroes/index.html', {'superheroes': superheroes})