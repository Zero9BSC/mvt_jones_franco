from django.db import models

# Create your models here.
class Tios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    
class Sobrinos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

class Bisabuelos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

class Bisnietos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()