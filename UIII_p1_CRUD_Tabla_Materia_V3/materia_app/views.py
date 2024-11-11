from django.shortcuts import render, redirect
from .models import Materia

# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request,'gestionarMateria.html', {"mismaterias":lasmaterias})

def registrarmateria(request):
    codido=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]
    guardarmateria=Materia.objects.create(codido=codido, nombre=nombre, credito=credito)

    return redirect('/')

def seleccionarmateria(request,codido):
    materia=Materia.objects.get(codido=codido)
    return render(request,"editarmateria.html", {"mismaterias":materia})

def borrarmateria(request,codido):
    materia=Materia.objects.get(codido=codido)
    materia.delete()

    return redirect('/')

def editarmateria(request):
    codido=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcreditos"]
    materia=Materia.objects.get(codido=codido)
    materia.nombre=nombre
    materia.credito=credito
    materia.save()
    return redirect('/')