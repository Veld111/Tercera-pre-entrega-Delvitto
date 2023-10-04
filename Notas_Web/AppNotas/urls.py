from django.urls import path
from AppNotas import views

urlpatterns = [
    path('', views.inicio),
    path('usuario/', views.usuario),
    path('notas/', views.notas),
    path('categoria/', views.categoria),

]
