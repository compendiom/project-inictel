from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.
def requestPage(request):
    anio = datetime.today().year
    plantillaExterna = open("D:\\proyectosVSC\\autenticador-certificados\\templates\\index.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    context = Context({"fecha": anio})
    document = template.render(context)
    return HttpResponse(document)

def errorPage(request):
    plantillaExterna = open("D:\proyectosVSC\\autenticador-certificados\\templates\error.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    context = Context()
    document = template.render(context)
    return  HttpResponse(document)

def responsePage(request):
    plantillaExterna = open("D:\proyectosVSC\\autenticador-certificados\\templates\\resultado.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    context = Context()
    document = template.render(context)
    return  HttpResponse(document)