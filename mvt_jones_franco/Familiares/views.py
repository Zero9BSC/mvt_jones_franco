#from django.shortcuts import render
from django.http import HttpResponse
from models import Padres
# Create your views here.
def mostar_familiares(request):
    madre = Padres(nombre='Marlen', apellido='Jones')
    saludo = f'Hola a todos esta es mi Familia {madre.nombre}'

    return HttpResponse
    #return render(request, '', {'nombre': madre, 'apellido': madre})
