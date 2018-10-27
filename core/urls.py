from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('adoptantes/', listar_adoptante, name="adoptantes"),
    path('home-cliente/', home_cliente, name="home_cliente"),
    path('formulario_adoptante/', formulario_adoptante , name="formulario_adoptante"),
    path('eliminar_adoptante/<id>/', eliminar_adoptante, name="eliminar_adoptante"),
    path('modificar_adoptante/<id>/', modificar_adoptante, name="modificar_adoptante"),
    path('mascotas/', listar_mascota, name="mascotas"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('formulario_mascota/', formulario_mascota, name="formulario_mascota"),

]

