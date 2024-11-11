from django.urls import path
from materia_app import views

urlpatterns = [
    path('',views.inicio_vista,name="inicio_vista"),
    path("registrarmateria/", views.registrarmateria, name="registrarmateria/"),
    path("borrarmateria/<codido>",views.borrarmateria, name="borrarmateria/"),
    path("seleccionarmateria/<codido>", views.seleccionarmateria, name="selecionarmateria/"),
    path("editarmateria/", views.editarmateria, name="editarmateria")
]
