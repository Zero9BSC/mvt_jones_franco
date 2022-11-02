from django.db import models

# Familiares de Primer Grado
class Padres(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    
class Hijos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

# Familiares de Segundo Grado
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

# Familiares de Tercer Grado
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

# Familiares de Cuarto Grado
class Primos_hermanos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

class Tios_abuelos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
