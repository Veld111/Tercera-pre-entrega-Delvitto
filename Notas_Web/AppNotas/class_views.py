from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CrearNota

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class CrearNotaListView(ListView):
    model = CrearNota
    template_name = "AppNotas/crear_nota_list.html"
    context_object_name = "notas"  # Nombre con el que se accederá a los datos en la plantilla


class CrearNotaDetailView(DetailView):
    model = CrearNota
    template_name = "AppNotas/crear_nota_detail.html"
    context_object_name = "nota"  # Nombre con el que se accederá al objeto en la plantilla

class CrearNotaCreateView(CreateView):
    model = CrearNota
    template_name = "AppNotas/crear_nota_create.html"
    fields = ["curso", "camada"]
    success_url = reverse_lazy("notas_guardadas")



class CrearNotaUpdateView(UpdateView):
    model = CrearNota
    template_name = "AppNotas/crear_nota_update.html"
    fields = ["curso", "camada"]
    success_url = reverse_lazy("List")


class CrearNotaDeleteView(DeleteView):
    model = CrearNota
    template_name = "AppNotas/crear_nota_confirm_delete.html"
    success_url = reverse_lazy("List")
