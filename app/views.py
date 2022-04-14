import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hola")

def inicio(request):
    return render (request, 'app/inicio.html')

def inicioError(request):
    return render (request, 'app/inicioError.html')

def menuDecano(request):
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