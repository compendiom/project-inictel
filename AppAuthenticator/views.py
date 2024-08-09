from datetime import datetime
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

from AppAuthenticator.models import Formulario

# Create your views here.
def requestPage(request):
    anio = datetime.today().year
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/response/")
        else:
            return HttpResponseRedirect("/error/")
    else:
        form = Formulario()
    return render(request, 'footer.html', {"fecha": anio, "form": form})

def errorPage(request):
    return render(request, 'error.html')

def responsePage(request):
    form = Formulario(request.POST)
    cursor=connection.cursor()
    cursor.callproc("[dbo].[SPU_VALIDACION_CLIENTE]", [form.apellido, form.dni])
    return render(request, 'resultado.html') 