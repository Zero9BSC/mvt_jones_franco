from django.shortcuts import render
#from django.http import HttpResponse
from .models import *


def mostar_familiares(request):
    #madre = Padres(nombre='Marlen', apellido='Jones')
    #saludo = f'Hola a todos esta es mi Familia {madre.nombre}'
    
    abuelo = Familiar(parentesco= 'Abuelo', nombre= 'Elder', apellido= 'Jones', dni='05122682', edad='85', fecha_de_nacimiento='18-07-1936')
    madre = Familiar(parentesco= 'Madre', nombre= 'Marlen', apellido= 'Jones', dni='18665444', edad='60', fecha_de_nacimiento='25-12-1962')
    esposa = Familiar(parentesco= 'Esposa', nombre= 'Marina', apellido= 'Arenas', dni='36225644', edad='30', fecha_de_nacimiento='15-06-1992')
    hijo1 = Familiar(parentesco= 'Hijo', nombre= 'Noah', apellido= 'Jones', dni='52668997', edad='10', fecha_de_nacimiento='30-11-2012')
    hijo2 = Familiar(parentesco= 'Hijo', nombre= 'Naomi', apellido= 'Jones', dni='56581897', edad='3', fecha_de_nacimiento='04-11-2012')


    return render(request, 'familiares1.html', {'objetos': [abuelo, madre, esposa, hijo1, hijo2]})
    #return HttpResponse(saludo)
    #return render(request, '', {'nombre': madre, 'apellido': madre})
