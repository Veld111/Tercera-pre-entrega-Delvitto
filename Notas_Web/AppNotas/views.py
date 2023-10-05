from django.shortcuts import render
from .models import CrearNota, NotasGuardadas, EliminarNota

def inicio(request):
    creador_notas = CrearNota.objects.all()
    notas_guardadas = NotasGuardadas.objects.all()
    eliminar_notas = EliminarNota.objects.all()
    return render(request, "AppNotas/index.html", {'creador_notas': creador_notas, 'notas_guardadas': notas_guardadas, 'eliminar_notas': eliminar_notas})

def crear_nota(request):
    return render(request, "AppNotas/crear_nota.html")

def notas_guardadas(request):
    return render(request, "AppNotas/notas_guardadas.html")

def eliminar_nota(request):
    return render(request, "AppNotas/eliminar_nota.html")
