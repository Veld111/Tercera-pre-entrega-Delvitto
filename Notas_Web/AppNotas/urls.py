from django.urls import path
from AppNotas import views
from AppNotas import class_views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_nota/', views.crear_nota, name='crear_nota'),
    path('notas_guardadas/', views.notas_guardadas, name='notas_guardadas'),
    path('eliminar_nota/', views.eliminar_nota, name='eliminar_nota'),
    path('crear_nota_form/', views.crear_nota_form, name='crear_nota_form'),
    path('apiform/', views.form_con_api, name="form_con_api"),
    path('buscar_notas/', views.buscar_notas, name='buscar_notas'),
]


# URL's basadas en clases
urlpatterns += [
    path('class-list/', class_views.CrearNotaListView.as_view(), name="List"),
    path('class-detail/<pk>/', class_views.CrearNotaDetailView.as_view(), name="Detail"),
    path('class-create/', class_views.CrearNotaCreateView.as_view(), name="Create"),
    path('class-update/<pk>/', class_views.CrearNotaUpdateView.as_view(), name="Update"),
    path('class-delete/<pk>/', class_views.CrearNotaDeleteView.as_view(), name="Delete"),
]
# objects.get(pk=pk)