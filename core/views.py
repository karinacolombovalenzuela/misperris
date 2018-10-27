from django.shortcuts import render, redirect
from .models import Adoptante, Region ,Vivienda ,Ciudad ,Raza ,Tipo ,Mascota 

from django.contrib import messages

from django.contrib.auth.decorators import login_required



# Create your views here.

# Create your views here.

def home (request):
    return render(request,'core/home.html')
@login_required
def home_cliente (request):
    return render(request,'core/home_cliente.html')

@login_required
def listar_adoptante(request):
    #obtenemos todos los automoviles desde la BBDD
    adoptante = Adoptante.objects.all()
    #le pasamos los postulantes al template
    #para que el los despliegue
    return render(request, 'core/listar_adoptante.html',{
        'adoptante':adoptante
    })


def formulario_adoptante(request):

    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    viviendas = Vivienda.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'regiones':regiones,
        'ciudades':ciudades,
        'viviendas':viviendas
    }
  
    #preguntamos si la peticion es POST, lo que quiere decir que el usuario
    #presiono el boton en el formulario
    if request.POST:
        #instanciamos un modelo Adoptante
        adoptante = Adoptante()
        adoptante.rut = request.POST.get('rut')
        adoptante.nombre = request.POST.get('nombre')
        adoptante.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        adoptante.email = request.POST.get('email')
        adoptante.telefono = int(request.POST.get('txtTelefono'))
        #instanciar un modelo Region
        region = Region()
        region.id = int(request.POST.get('cboRegion'))
        #le pasamos el modelo region al Adoptante
        adoptante.region = region
        #instanciar un modelo Ciudad
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        #le pasamos el modelo ciudad al Adoptante
        adoptante.ciudad = ciudad
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        #le pasamos el modelo vivienda al Adoptante
        adoptante.vivienda = vivienda

        try:
            adoptante.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/formulario_adoptante.html',variables)
@login_required
def eliminar_adoptante(request, id):

    #para eliminar es necesario primero buscar el automovil
    adoptante = Adoptante.objects.get(id=id)

    #una vez encontrado el automovil se procede a eliminarlo
    try:
        adoptante.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="adoptantes")
@login_required
def modificar_adoptante(request, id):

    region = Region.objects.all()
    ciudad = Ciudad.objects.all()
    vivienda = Vivienda.objects.all()
    #buscamos el adoptante en la BBDD por su ID
    adoptante = Adoptante.objects.get(id=id)
    variables = {
        'region':region,
        'ciudad':ciudad,
        'vivienda':vivienda,
        'adoptante':adoptante
    }

    if request.POST:
        #si la peticion es POST recibimos las variables
        adoptante = Adoptante()
        adoptante.id = int(request.POST.get('txtId'))
        adoptante.rut = request.POST.get('rut')
        adoptante.nombre = request.POST.get('nombre')
        adoptante.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        adoptante.email = request.POST.get('email')
        adoptante.telefono = int(request.POST.get('txtTelefono'))
        #instanciar un modelo Region
        region = Region()
        region.id = int(request.POST.get('cboRegion'))
        #le pasamos el modelo region al Adoptante
        adoptante.region = region
        #instanciar un modelo Ciudad
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        #le pasamos el modelo ciudad al Adoptante
        adoptante.ciudad = ciudad
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        #le pasamos el modelo vivienda al Adoptante
        adoptante.vivienda = vivienda
        try:
            auto.save()
            messages.success(request, "Actualizado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")

        #le haremos un redirect al usuario de vuelta hacia el listado   
        return redirect('adoptantes')

    return render(request, 'core/modificar_adoptante.html', variables)
@login_required
def listar_mascota(request):
    #obtenemos todos los mascota desde la BBDD
    mascota = Mascota.objects.all()
    #le pasamos los postulantes al template
    #para que el los despliegue
    return render(request, 'core/listar_mascota.html',{
        'mascota':mascota
        
    })
@login_required
def formulario_mascota(request):

    razas = Raza.objects.all()
    tipos = Tipo.objects.all()
    #declaramos las variables que se enviarán al template
    variables = {
        'razas':razas, 
        'tipos':tipos
    }
    


    #preguntamos si la peticion es POST, lo que quiere decir que el usuario
    #presiono el boton en el formulario
    if request.POST:
        #instanciamos un modelo Adoptante
        mascota = Mascota()
        mascota.nombre = request.POST.get('nombre')
        mascota.genero = request.POST.get('genero')
        mascota.fechaIngreso = request.POST.get('FechaIngreso')
        mascota.fechaNacimiento = request.POST.get('FechaNacimiento')
        mascota.descripcion = request.POST.get('descripcion')
        mascota.model_pic = request.FILES.get('image')
        raza = Raza()
        raza.id = int(request.POST.get('raza'))
        mascota.raza = raza
        tipo = Tipo()
        tipo.id = int(request.POST.get('cboTipo'))
        mascota.tipo = tipo
        mascota.save()
        try:
            
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/formulario_mascota.html',variables)
@login_required
def eliminar_mascota(request, id):

    #para eliminar es necesario primero buscar el mascota
    mascota = Mascota.objects.get(id=id)

    #una vez encontrado la mascota se procede a eliminarlo
    try:
        mascota.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="mascota")

   
@login_required
def modificar_mascota(request, id):

    raza = Raza.objects.all()
    tipo = Tipo.objects.all()
    #buscamos el adoptante en la BBDD por su ID
    mascota = Mascota.objects.get(id=id)
    variables = {
        'raza':raza,
        'tipo':tipo,
        'mascota':mascota
    }

    if request.POST:
   
        #si la peticion es POST recibimos las variables
        mascota = Mascota()
        mascota.id = int(request.POST.get('txtId'))
        mascota.nombre = request.POST.get('nombre')
        #instanciar un modelo Raza
        raza = Raza()
        raza.id = int(request.POST.get('cboRaza'))
        #le pasamos el modelo raza a mascota
        mascota.raza = raza
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaingreso = request.POST.get('fechaIngreso')
        mascota.fechaNacimiento = request.POST.get('fechaNacimiento')
        mascota.descripcion = request.POST.get('txtDescripcion')
        mascota.imagen = request.POST.get('imagen')
        #instanciar un modelo Estado
        tipo = Tipo()
        tipo.id = int(request.POST.get('cboTipo'))
        #le pasamos el modelo estado a mascota
        mascota.tipo = tipo
        try:
            mascota.save()
            messages.success(request, "Actualizado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")

        #le haremos un redirect al usuario de vuelta hacia el listado   
        return redirect('mascotas')

    return render(request, 'core/modificar_mascota.html', variables)


