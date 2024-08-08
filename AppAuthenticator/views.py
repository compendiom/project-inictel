from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def requestPage(request):
    anio = datetime.today().year
    return render(request, 'footer.html', {"fecha": anio})

def errorPage(request):
    return render(request, 'error.html')

def responsePage(request):
    return render(request, 'resultado.html') 