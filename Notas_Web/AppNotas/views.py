from django.shortcuts import render
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

def inicio(request):
    formulario = BuscarNotasForm()
    resultados = []

    if request.method == "POST":
        formulario = BuscarNotasForm(request.POST)
        if formulario.is_valid():
            termino_busqueda = formulario.cleaned_data['termino_busqueda']
            # Realiza la búsqueda en tu base de datos
            resultados = NotasGuardadas.objects.filter(titulo__icontains=termino_busqueda)

    return render(request, "AppNotas/index.html", {"formulario": formulario, "resultados": resultados})



def buscar_notas(request):
    resultados = []
    formulario = BuscarNotasForm()  # Crear una instancia del formulario vacío

    if request.method == "POST":
        formulario = BuscarNotasForm(request.POST)
        if formulario.is_valid():
            termino_busqueda = formulario.cleaned_data['termino_busqueda']
            # Realiza la búsqueda en tu base de datos
            resultados = CrearNota.objects.filter(titulo__icontains=termino_busqueda)

    return render(request, "AppNotas/resultados_buscar_notas.html", {"resultados": resultados, "formulario": formulario})



def crear_nota_form(request):
    if request.method == 'POST':
        # Modificamos aquí para que capture los datos de nombre y apellido en lugar de curso y camada
        formulario = CrearNotaForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            crearnota = CrearNota(nombre=informacion["nombre"], apellido=informacion["apellido"])
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
            crearnota = CrearNota(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            crearnota.save()
            return render(request, "AppNotas/index.html")
    else:
        miFormulario = CrearNotaForm()

    return render(request, "AppNotas/form_con_api.html", {"miFormulario": miFormulario})

"""def crear_nota_form(request):
      if request.method == 'POST':
      
            curso =  CrearNota(request.post['curso'],(request.post['camada']))
 
            curso.save()
 
            return render(request, "AppNotas/index.html")
 
      return render(request, 'AppNotas/crear_nota_form.html')


def form_con_api(request):
    if request.method == "POST":
        miFormulario = CrearNotaForm(request.POST)  # Usa el formulario definido
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = CrearNota(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppNotas/index.html")
    else:
        miFormulario = CrearNotaForm()

    return render(request, "AppNotas/form_con_api.html", {"miFormulario": miFormulario})

"""
"""def crear_nota_form(request):
    if request.method == 'POST':
        form = CrearNotaForm(request.POST)  # Crea una instancia del formulario con los datos POST

        if form.is_valid():
            # Guarda el formulario si es válido
            form.save()
            # Puedes redirigir a la página de éxito o a donde lo necesites
            return redirect('AppNotas/index.html')
    else:
        form = CrearNotaForm()  # Crea una instancia vacía del formulario

    return render(request, 'AppNotas/crear_nota_form.html')"""
