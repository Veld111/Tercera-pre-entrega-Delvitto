# models.py
from django.db import models

class CrearNota(models.Model):
    titulo = models.CharField(max_length=100, default="Sin título")

class NotasGuardadas(models.Model):
    titulo = models.CharField(max_length=100, default="Sin título")

class EliminarNota(models.Model):
    titulo = models.CharField(max_length=100, default="Sin título")
