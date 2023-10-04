from django.shortcuts import render

def inicio(request):
    return render(request, "AppNotas/index.html")

def usuario(request):
    return render(request, "AppNotas/usuario.html")

def notas(request):
    return render(request, "AppNotas/notas.html")

def categoria(request):
    return render(request, "AppNotas/categoria.html")
