from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import Decano, Facultad, Estudiante, EstadoVotacion, TipoVotacion, Votacion,Candidato, Voto
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
    try:
    # retorna la facultad del decano
        id_usuario=request.user.id
        facultad=Decano.objects.get(user_id=id_usuario)
        contexto={
            'Facultad':facultad
        }
        return render (request,'app/agregarEstudiante.html',contexto)
    except:
        veri=True
        return render (request, 'app/agregarEstudiante.html')
        
# # registro de estudiante
# def registro(request):
#     return render (request, 'app/listaDeEstudiantes.html')

def registroPost(request):
    #VALIDACION DE LOS DATOS
    try:
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
    except:
        veri=True
        return redirect('app:listaDeEstudiantes')

@login_required
def agregarEstudianteError(request):
    return render (request, 'app/agregarEstudianteError.html')

@login_required
def crearVotacion(request):
    try:
        # retorna la facultad del decano
        id_usuario=request.user.id
        Facultad=Decano.objects.get(user_id=id_usuario)

        # retorna tipos de votacion
        semestre=TipoVotacion.objects.get(id=1)
        facultad=TipoVotacion.objects.get(id=2)
        estado=EstadoVotacion.objects.get(id=1)
        # estado de la votacion
        contexto={
            'Facultad':Facultad,
            's':semestre,
            'f':facultad,
            'estado':estado
        }
        return render (request,'app/crearVotacion.html',contexto)
    except:
        veri=True
        return render (request, 'app/crearVotacion.html')

def votacionPost(request):
    
    # try:
    # saca datos
        Nombre=request.POST['nombre']
        FechaInicio=request.POST['fechaInicio']
        FechaFin=request.POST['fechaFin']
        # Tipo=request.POST['tipo']
        # el estado es postulacion
       
        #id de la facultad del decano (facultad.id)
        id_usuario=request.user.id
        facultad=Decano.objects.get(user_id=id_usuario)

        # crea votacion
        votacion=Votacion()
        estado=EstadoVotacion.objects.get(id=1)
        tipo=TipoVotacion.objects.get(id=1)

        votacion.nombre=Nombre
        votacion.estado_id=estado.id
        votacion.facultad_id=facultad.id
        votacion.fechaInicio=FechaInicio
        votacion.fechaFinal=FechaFin

        # tipo votacion
        votacion.tipo_id= tipo.id
        votacion.save()

        return redirect('app:listaDeVotaciones')
    # except:
    #     veri=True
    #     return redirect('app:listaDeVotaciones')

@login_required
def listaDeEstudiantes(request):  
    try:
        # id del la facultad del decano
        id_usuario=request.user.id
        facultad_decano=Decano.objects.get(user_id=id_usuario)
        
        lista=Estudiante.objects.filter(facultad_id=facultad_decano.id)
        
        contexto={
            'Estudiantes':lista
        }
        return render (request, 'app/listaDeEstudiantes.html',contexto)
    except:
        veri= True
        return render(request, 'app/listaDeEstudiantes.html')


@login_required
def listaDeVotaciones(request):
    try:
        # id del la facultad del decano
        id_usuario=request.user.id
        facultad_decano=Decano.objects.get(user_id=id_usuario)
        
        lista=Votacion.objects.filter(facultad_id=facultad_decano.id)
        
        contexto={
            'votaciones':lista
        }
        return render (request, 'app/listaDeVotaciones.html',contexto)
    except:
        veri= True
        return render(request, 'app/listaDeVotaciones.html')
    

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