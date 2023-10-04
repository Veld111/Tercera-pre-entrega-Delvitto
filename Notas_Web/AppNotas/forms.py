from django import forms
from .models import Usuario, Nota, Categoria

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class NotaForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())  # Puedes usar un ModelChoiceField para seleccionar un usuario existente.

class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea)
