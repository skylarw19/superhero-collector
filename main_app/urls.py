from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('superheroes/', views.superheroes_index, name='index'),
    path('superheroes/<int:superhero_id>/', views.superheroes_detail, name='detail'),
    path('superheroes/create/', views.SuperheroCreate.as_view(), name='superheroes_create'),
    path('superheroes/<int:pk>/update', views.SuperheroUpdate.as_view(), name='superheroes_update'), #by convention, CBVs that work with individ model instances will expect to find parameter named pk (so we don't use superhero_id)
    path('superheroes/<int:pk>/delete', views.SuperheroDelete.as_view(), name='superheroes_delete'),
]
