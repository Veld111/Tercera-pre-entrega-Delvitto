from django.contrib import admin
from .models import CrearNota, NotasGuardadas, EliminarNota

admin.site.register(CrearNota)
admin.site.register(NotasGuardadas)
admin.site.register(EliminarNota)
