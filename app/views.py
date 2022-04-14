import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return HttpResponse("Hola")

def inicio(request):
    return render (request, 'app/inicio.html')

def inicioPost(request):
    # recuperar datos
    u= request.POST['username']
    p= request.POST['password']
    #autentificacion de datos
    usuario= authenticate(username=u, password=p)
    
    if usuario is None:
        return render (request, 'app/inicioError.html')
    else:
        # inicia sesion
        login(request, usuario)
        print(usuario)
    return redirect('app:menuDecano')

def inicioError(request):
    return render (request, 'app/inicioError.html')

def salir(request):
    # cierra la sesion
    logout(request)
    return redirect('app:inicio')

def menuDecano(request):
    return render (request, 'app/menuDecano.html')

def agregarEstudiante(request):
    return render (request, 'app/agregarEstudiante.html')

def agregarEstudianteError(request):
    return render (request, 'app/agregarEstudianteError.html')

def crearVotacion(request):
    return render (request, 'app/crearVotacion.html')

def listaDeEstudiantes(request):
    return render (request, 'app/listaDeEstudiantes.html')

def listaDeVotaciones(request):
    return render (request, 'app/listaDeVotaciones.html')

def editarVotacion(request):
    return render (request, 'app/editarVotacion.html')

def vistaVotacionFacultad(request):
    return render (request, 'app/vistaVotacionFacultad.html')

def vistaVotacionSemestre(request):
    return render (request, 'app/vistaVotacionSemestre.html')

def postulacionEstudiante2(request):
    return render (request, 'app/postulacionEstudiante2.html')