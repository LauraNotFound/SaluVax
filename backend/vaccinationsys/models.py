from enum import unique
from django.db import models
from django.db.models.functions import Length
from django.utils.module_loading import module_dir

# Create your models here.
class Lote(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.nombre)

class Vial(models.Model):
    nombre = models.CharField(max_length=255)
    kit = models.CharField(max_length=255)
    enfermedad = models.CharField(max_length=255)
    fecha_caducidad = models.DateField()
    
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.nombre)

class Paciente(models.Model): 
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.CharField(max_length=255, unique=True) 
    direccion = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"

class Rol(models.Model):
    nombre = models.CharField(max_length=255) # solo puede ser medico o inventarista

    def __str__(self) -> str:
        return str(self.nombre)

class Usuario(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"

class Vacuna(models.Model):
    dosis_ml = models.DecimalField(decimal_places=2)
    fecha_inyeccion = models.DateField()

    vial = models.ForeignKey(Vial, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Vacuna ({self.fecha_inyeccion}): {self.dosis_ml}ml for {self.paciente}"

