from django import forms
from django.db import models

class BuscarNotasForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100, required=False)   # Campo para ingresar el título de la nota a buscar

class CrearNotaForm(forms.Form):
    titulo = forms.CharField(max_length=100)

class NotasGuardadasForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100)

class EliminarNotaForm(models.Model):
    titulo = models.CharField(max_length=100, default="Sin título")
