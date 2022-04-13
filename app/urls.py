from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'), 
    path('inicio/', views.inicio, name='inicio'),
    path('menuDecano/', views.menuDecano, name='menuDecano'),
    path('agregarEstudiante/', views.agregarEstudiante, name='agregarEstudiante'),
    path('crearVotacion/', views.crearVotacion, name='crearVotacion'),
    path('listaDeEstudiantes/', views.listaDeEstudiantes, name='listaDeEstudiantes'),
    path('listaDeVotaciones/', views.listaDeVotaciones, name='listaDeVotaciones'),
]