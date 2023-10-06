from django import forms
from .models import CrearNota  # Asegúrate de importar el modelo adecuado
from django import forms

class BuscarNotasForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, required=False)   # Campo para ingresar el título de la nota a buscar

class CrearNotaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.CharField(max_length=40)
# Formulario para guardar notas
class NotasGuardadasForm(forms.ModelForm):
    creador = forms.ModelChoiceField(queryset=CrearNota.objects.all())
    titulo = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)

# Formulario para eliminar notas
class EliminarNotaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
