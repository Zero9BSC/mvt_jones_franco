from django.db import models

# Familiares de Primer Grado
class Familiar(models.Model):
    parentesco = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()