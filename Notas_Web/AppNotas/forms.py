from django import forms

class BuscarNotasForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, required=False)   # Campo para ingresar el título de la nota a buscar

class CrearNotaForm(forms.Form):
    titulo = forms.CharField(max_length=100)

# Formulario para guardar notas
class NotasGuardadasForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100)

from django.db import models

class EliminarNotaForm(models.Model):
    titulo = models.CharField(max_length=100, default="Sin título")
