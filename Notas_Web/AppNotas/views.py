from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppNotas/index.html")

def usuario(request):
    return HttpResponse("Vista usuario")

def notas(request):
    return HttpResponse("Vista notas")

def categoria(request):
    return HttpResponse("Vista categoría")

