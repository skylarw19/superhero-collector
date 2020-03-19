from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('superheroes/', views.superheroes_index, name='index'),
    path('superheroes/<int:superhero_id>/', views.superheroes_detail, name='detail'),
    path('superheroes/create/', views.CatCreate.as_view, name='cats_create'),
]
