from django.shortcuts import render
from AppNotas.forms import CrearNotaForm, BuscarNotasForm
from .models import CrearNota, NotasGuardadas

def inicio(request):
    return render(request, "AppNotas/index.html")

def crear_nota(request):
    return render(request, "AppNotas/crear_nota.html")

def notas_guardadas(request):
    return render(request, "AppNotas/notas_guardadas.html")

def eliminar_nota(request):
    return render(request, "AppNotas/eliminar_nota.html")

def buscar_notas(request):
    resultados = []

    if request.method == "POST":
        formulario = BuscarNotasForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            termino_busqueda = informacion["termino_busqueda"]
            resultados = NotasGuardadas.objects.filter(titulo__icontains=termino_busqueda)
    else:
        formulario = BuscarNotasForm()

    return render(request, "AppNotas/buscar_notas_form.html", {"resultados": resultados, "formulario": formulario})

def crear_nota_form(request):
    if request.method == 'POST':
        formulario = CrearNotaForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            crearnota = CrearNota(titulo=informacion["titulo"])
            crearnota.save()
            return render(request, "AppNotas/index.html")
    else:
        formulario = CrearNotaForm()

    return render(request, 'AppNotas/crear_nota_form.html', {"miFormulario": formulario})


