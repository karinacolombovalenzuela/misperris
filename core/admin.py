from django.contrib import admin
from .models import Adoptante, Region, Ciudad, Vivienda ,Mascota ,Raza ,Tipo

# Register your models here.

class AdoptanteAdmin(admin.ModelAdmin):
    #las tuplas con como arreglos pero no se pueden modificar
    list_display = ('rut', 'nombre', 'fechaNacimiento', 'email', 'telefono')
    search_fields = ['rut', 'nombre']

class MascotaAdmin(admin.ModelAdmin):
    #las tuplas con como arreglos pero no se pueden modificar
    list_display = ('nombre', 'genero', 'fechaIngreso', 'fechaNacimiento', 'descripcion', 'model_pic')
    search_fields = ['nombre', 'fechaIngreso']
   
 

admin.site.register(Adoptante, AdoptanteAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Vivienda)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Raza)
admin.site.register(Tipo)



