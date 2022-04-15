from multiprocessing import context
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import Decano, Facultad, Estudiante
from django.contrib.auth.decorators import login_required

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
        return redirect('app:menuDecano')

def inicioError(request):
    return render (request, 'app/inicioError.html')

def salir(request):
    # cierra la sesion
    logout(request)
    return redirect('app:inicio')

@login_required
def menuDecano(request):
    return render (request, 'app/menuDecano.html')

@login_required
def agregarEstudiante(request):

    # retorna la facultad del decano
        id_usuario=request.user.id
        facultad=Decano.objects.get(user_id=id_usuario)
        contexto={
            'Facultad':facultad
        }
        return render (request, 'app/agregarEstudiante.html',contexto)

# registro de estudiante
def registro(request):
    return render (request, 'app/listaDeEstudiantes.html')

def registroPost(request):
    #VALIDACION DE LOS DATOS
   
    # saca datos
    nombre=request.POST['nombres']
    apellidos=request.POST['apellidos']
    username=request.POST['username']
    semestre=request.POST['semestre']
    email=request.POST['email']
    documento=request.POST['documento']
    
    # se obtiene el id de la facultad del estudiante
    id_usuario=request.user.id
    facultad=Decano.objects.get(user_id=id_usuario)
    #crea usuario
    usuario=User()
    usuario.first_name=nombre
    usuario.last_name=apellidos
    usuario.username=username
    usuario.email=email
    usuario.set_password(documento)
    usuario.save()

    estudiante=Estudiante()
    estudiante.semestreActual=semestre
    estudiante.user_id=usuario.id
    estudiante.facultad_id=facultad.id
    estudiante.save()

    return redirect('app:listaDeEstudiantes')



@login_required
def agregarEstudianteError(request):
    return render (request, 'app/agregarEstudianteError.html')

@login_required
def crearVotacion(request):
    return render (request, 'app/crearVotacion.html')

@login_required
def listaDeEstudiantes(request):
    return render (request, 'app/listaDeEstudiantes.html')

@login_required
def listaDeVotaciones(request):
    return render (request, 'app/listaDeVotaciones.html')

@login_required
def editarVotacion(request):
    return render (request, 'app/editarVotacion.html')

@login_required
def vistaVotacionFacultad(request):
    return render (request, 'app/vistaVotacionFacultad.html')

@login_required
def vistaVotacionSemestre(request):
    return render (request, 'app/vistaVotacionSemestre.html')

@login_required
def postulacionEstudiante2(request):
    return render (request, 'app/postulacionEstudiante2.html')