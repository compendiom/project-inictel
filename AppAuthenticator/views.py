from datetime import datetime
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render

from AppAuthenticator.models import Curso, Formulario

# Create your views here.
def requestPage(request):
    anio = datetime.today().year
    submitted = False
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return 
        else:
            #error_message = "El datos enviado en el formulario no son válidos o no se encuentran en la base de datos"
            return 
    else:
        form = Formulario()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'footer.html', {"fecha": anio, "form": form, "submitted": submitted})

def errorPage(request):
    return render(request, 'error.html')

def responsePage(request, apellido, dni):
    cursor=connection.cursor()
    curso = Curso.objects.get()
    try:
        cursor.callproc("[dbo].[SPU_VALIDACION_CLIENTE]", [apellido, dni])
        if cursor.return_value == 1:
            result_set = cursor.fetchall()
    except:
        return HttpResponseRedirect('/error')
    finally:
        cursor.close()
    return render(request, 'resultado.html', {"result_set": result_set}) 