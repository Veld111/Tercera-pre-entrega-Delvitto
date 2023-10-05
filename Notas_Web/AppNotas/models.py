from django.db import models

class CrearNota(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class NotasGuardadas(models.Model):
    creador = models.ForeignKey(CrearNota, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class EliminarNota(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
