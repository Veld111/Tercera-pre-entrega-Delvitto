from django.shortcuts import render
from .models import CrearNota, NotasGuardadas, EliminarNota

def inicio(request):
    return render(request, "AppNotas/index.html")

def crear_nota(request):
    return render(request, "AppNotas/crear_nota.html")

def notas_guardadas(request):
    return render(request, "AppNotas/notas_guardadas.html")

def eliminar_nota(request):
    return render(request, "AppNotas/eliminar_nota.html")
