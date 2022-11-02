from django.db import models

# Create your models here.
class Padres(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    
class Hijos(models.Model):