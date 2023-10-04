from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario, Nota, Categoria
from .forms import NotaFormulario, CategoriaFormulario

class UsuarioListView(ListView):
    model = Usuario
    template_name = "AppNotas/usuario_list.html"

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = "AppNotas/usuario_detail.html"

class NotaCreateView(CreateView):
    model = Nota
    template_name = "AppNotas/nota_create.html"
    form_class = NotaFormulario
    success_url = reverse_lazy("notas_list")

class NotaUpdateView(UpdateView):
    model = Nota
    template_name = "AppNotas/nota_update.html"
    form_class = NotaFormulario
    success_url = reverse_lazy("notas_list")

class NotaDeleteView(DeleteView):
    model = Nota
    template_name = "AppNotas/nota_delete.html"
    success_url = reverse_lazy("notas_list")

class CategoriaListView(ListView):
    model = Categoria
    template_name = "AppNotas/categoria_list.html"

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "AppNotas/categoria_detail.html"

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "AppNotas/categoria_create.html"
    form_class = CategoriaFormulario
    success_url = reverse_lazy("categorias_list")

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "AppNotas/categoria_update.html"
    form_class = CategoriaFormulario
    success_url = reverse_lazy("categorias_list")

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "AppNotas/categoria_delete.html"
    success_url = reverse_lazy("categorias_list")
