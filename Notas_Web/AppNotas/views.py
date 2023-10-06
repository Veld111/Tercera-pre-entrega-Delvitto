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
    resultados = []  # Inicializamos una lista vacía para almacenar los resultados

    if request.method == "POST":
        formulario = BuscarNotasForm(request.POST)  # Utiliza el formulario de búsqueda que creamos

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            termino_busqueda = informacion["termino_busqueda"]

            # Realiza la búsqueda en tu base de datos utilizando objects.filter en el modelo NotasGuardadas
            resultados = NotasGuardadas.objects.filter(titulo__icontains=termino_busqueda)

    else:
        formulario = BuscarNotasForm()

    return render(request, "AppNotas/resultados_buscar_notas.html", {"resultados": resultados, "formulario": formulario})

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


def form_con_api(request):
    if request.method == "POST":
        miFormulario = CrearNotaForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            crearnota = CrearNota(titulo=informacion["titulo"])
            crearnota.save()
            return render(request, "AppNotas/index.html")
    else:
        miFormulario = CrearNotaForm()

    return render(request, "AppNotas/form_con_api.html", {"miFormulario": miFormulario})