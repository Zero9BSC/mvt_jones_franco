from django.db import models

# Create your models here.
class Abuelos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    
class Nietos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

class Hermanos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()