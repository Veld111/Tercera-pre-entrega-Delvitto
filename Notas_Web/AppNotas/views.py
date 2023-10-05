from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CrearNotaForm  # Asegúrate de importar el formulario adecuado


def inicio(request):
    return render(request, "AppNotas/index.html")

def crear_nota(request):
    return render(request, "AppNotas/crear_nota.html")

def notas_guardadas(request):
    return render(request, "AppNotas/notas_guardadas.html")

def eliminar_nota(request):
    return render(request, "AppNotas/eliminar_nota.html")

def crear_nota_form(request):
    if request.method == 'POST':
        form = CrearNotaForm(request.POST)  # Crea una instancia del formulario con los datos POST

        if form.is_valid():
            # Guarda el formulario si es válido
            form.save()
            # Puedes redirigir a la página de éxito o a donde lo necesites
            return redirect('AppNotas/index.html')
    else:
        form = CrearNotaForm()  # Crea una instancia vacía del formulario

    return render(request, 'AppNotas/crear_nota_form.html')
