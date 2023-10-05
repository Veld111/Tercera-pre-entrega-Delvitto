from django import forms
from .models import CrearNota  # Asegúrate de importar el modelo adecuado

class CrearNotaForm(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

# Formulario para guardar notas
class NotasGuardadasForm(forms.ModelForm):
    creador = forms.ModelChoiceField(queryset=CrearNota.objects.all())
    titulo = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)

# Formulario para eliminar notas
class EliminarNotaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
