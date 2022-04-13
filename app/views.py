from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola")

def inicio(request):
    return render (request, 'app/inicio.html')

def menuDecano(request):
    return render (request, 'app/menuDecano.html')

def agregarEstudiante(request):
    return render (request, 'app/agregarEstudiante.html')

def crearVotacion(request):
    return render (request, 'app/crearVotacion.html')

def listaDeEstudiantes(request):
    return render (request, 'app/listaDeEstudiantes.html')

def listaDeVotaciones(request):
    return render (request, 'app/listaDeVotaciones.html')