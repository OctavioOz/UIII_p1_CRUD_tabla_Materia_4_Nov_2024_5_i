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