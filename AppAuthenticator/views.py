from datetime import datetime
from pyexpat.errors import messages
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from autenticator import settings
from AppAuthenticator.models import Persona

# Create your views here.
def requestPage(request):
    anio = datetime.today().year
    form = Persona()
    if request.method == 'POST':
        form = Persona(request, data=request.POST)
        if form.is_valid():
            apellido=request.GET['apellido']
            dni=request.GET['dni']
    return render(request, 'footer.html', {"fecha": anio, "form": form})

def errorPage(request, error_message=None):
    if error_message == None:
        error_message = "Error en la base de datos"
    return render(request, 'error.html', {'error': error_message})

def responsePage(request, apellido=None, dni=None):

    return render(request, 'resultado.html') 