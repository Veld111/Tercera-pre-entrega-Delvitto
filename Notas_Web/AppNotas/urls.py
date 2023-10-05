from django.urls import path
from AppNotas import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_nota/', views.crear_nota, name='crear_nota'),
    path('notas_guardadas/', views.notas_guardadas, name='notas_guardadas'),
    path('eliminar_nota/', views.eliminar_nota, name='eliminar_nota'),
    path('crear_nota_form/', views.crear_nota_form, name='crear_nota_form'),
]
