from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.index, name='index'), 
    path('inicio/', views.inicio, name='inicio'),
    path('inicioPost',views.inicioPost, name='inicioPost'),
    path('salir',views.salir, name='salir'),
    path('inicioError/', views.inicioError, name='inicioError'),
    path('menuDecano/', views.menuDecano, name='menuDecano'),
    path('agregarEstudiante/', views.agregarEstudiante, name='agregarEstudiante'),
    path('registro/',views.registro,name='registro'),
    path('registroPost/',views.registroPost,name='registroPost'),
    path('agregarEstudianteError/', views.agregarEstudianteError, name='agregarEstudianteError'),
    path('crearVotacion/', views.crearVotacion, name='crearVotacion'),
    path('listaDeEstudiantes/', views.listaDeEstudiantes, name='listaDeEstudiantes'),
    path('listaDeVotaciones/', views.listaDeVotaciones, name='listaDeVotaciones'),
    path('editarVotacion/', views.editarVotacion, name='editarVotacion'),
    path('vistaVotacionFacultad/', views.vistaVotacionFacultad, name='vistaVotacionFacultad'),
    path('vistaVotacionSemestre/', views.vistaVotacionSemestre, name='vistaVotacionSemestre'),
    path('postulacionEstudiante2/', views.postulacionEstudiante2, name='postulacionEstudiante2'),

]