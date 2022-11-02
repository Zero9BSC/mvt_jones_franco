from django.http import HttpResponse
from django.shortcuts import render

def familiares(request):
    return render(request, 'hola.html', {'nombre': 'Marlen'})