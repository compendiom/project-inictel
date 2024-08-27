from datetime import datetime
from pyexpat.errors import messages
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from . import db
from autenticator import settings
from AppAuthenticator.models import PersonaForm

# Create your views here.
def requestPage(request):
    anio = datetime.today().year
    form = PersonaForm()
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            recaptcha_response=request.POST.get('g-recaptcha-response')
            data = {
                'secret' : settings.RECAPTCHA_PRIVATE_KEY,
                'response' : recaptcha_response
            }
            req = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = req.json()
            if result['success']:
                dni = form.cleaned_data.get('dni')
                # Conexión a la base de datos
                result = db.connectDB()
                if result is False:
                    return render(request, 'error.html', {"error_message": "Error al conectar la base de datos"})
                # Validar información
                result = db.validateInfo(dni, form.cleaned_data.get('apellido'))
                if result is False:
                    return render(request, 'error.html', {'error_message': 'Error en la validación de usuario buscado'})
                nombre = result
                # Validar cursos
                result = db.getValidatedCursos(dni, form.cleaned_data.get('codigo'), form.cleaned_data.get('tipo'))
                if result is False:
                    return render(request, 'error.html', {'error_message': 'No se encontraron coincidencias con la base datos'})
                curso = result
                print(curso)
                return render(request, 'resultado.html', {"Nombre": nombre, "dni": dni, "curso": curso})
            else:
                return render(request, 'error.html', {"error_message": "Error en el Captcha"})
    return render(request, 'footer.html', {"anio": anio, "form": form})

def errorPage(request, error_message=None):
    if error_message == None:
        error_message = "Error no identificado, vuelva a intentarlo. Si sigue el mismo error comunicar a soporte técnico"
    return render(request, 'error.html', {'error_message': error_message})

def responsePage(request, apellido=None, dni=None):
    return render(request, 'resultado.html')