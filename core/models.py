from django.db import models

# Create your models here.


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
    

    def __str__(self):
        return self.ciudad

class Region(models.Model):
    region = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.region


class Vivienda(models.Model):
    vivienda = models.CharField(max_length=50)
   
    def __str__(self):
        return self.vivienda

class Adoptante(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    fechaNacimiento = models.DateField(max_length=10)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)

    def formato_fechaNacimiento(self):
        return self.fechaNacimiento.strftime("%Y-%m-%d")
 
    class Meta:
        verbose_name = "Adoptante"
        verbose_name_plural = "Adoptantes"
    
    def __str__(self):
        return self.rut


class Raza(models.Model):
    raza = models.CharField(max_length=50)

    def __str__(self):
        return self.raza

class Tipo(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo



class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fechaIngreso = models.DateField(max_length=10)
    fechaNacimiento = models.DateField(max_length=10)
    descripcion = models.CharField(max_length=50)
    model_pic = models.ImageField(upload_to = 'pic_folder/')  
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)


    def formato_fechaIngreso(self):
        return self.fechaIngreso.strftime("%Y-%m-%d")
    
    def formato_fechaNacimiento(self):
        return self.fechaNacimiento.strftime("%Y-%m-%d")
   
    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
    
    def __str__(self):
        return self.nombre

