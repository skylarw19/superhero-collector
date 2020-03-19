from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Superhero

#CBV
class SuperheroCreate(CreateView):
    model = Superhero
    fields = '__all__'
    # success_url = '/superheroes/'

class SuperheroUpdate(UpdateView):
    model = Superhero
    fields = ['power', 'description', 'age']

class SuperheroDelete(DeleteView):
    model = Superhero
    success_url = '/superheroes/'

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def superheroes_index(request):
    superheroes = Superhero.objects.all()
    return render(request, 'superheroes/index.html', {'superheroes': superheroes})

def superheroes_detail(request, superhero_id):
  superhero = Superhero.objects.get(id=superhero_id)
  return render(request, 'superheroes/detail.html', { 'superhero': superhero })