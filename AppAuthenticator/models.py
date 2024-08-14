from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

# Create your models here.
class Curso(models.Model):
    #nombreCurso = models.CharField(max_length=160)
    programa = models.CharField(max_length=255)
    #nota = models.CharField(max_length=5)
    #horas = models.CharField(max_length=2)´
class Persona(models.Model):
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=11)

class PersonaForm(ModelForm):
    class Meta:
        model=Persona
        fields = "__all__"
        widgets = {
            'apellido': forms.TextInput(attrs={'type':'text', 'pattern':'[A-ZÑ]+', 'name': 'apellido', 'placeholder': 'PEREZ', 'title': 'Este campo debe tener SOLO letras mayúsculas', 'required': 'true'}),
            'dni': forms.TextInput(attrs={'type':'text', 'pattern':'.{8}', 'name': 'dni', 'placeholder': '12345678', 'title': 'Este campo debe tener 8 dígitos numéricos', 'required': 'true'})
        }
    #apellido = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'type':'text', 'pattern':'[A-ZÑ]+', 'name': 'apellido', 'placeholder': 'PEREZ', 'title': 'Este campo debe tener SOLO letras mayúsculas'}))
    #dni = forms.CharField(required=True, max_length=11, widget=forms.TextInput(attrs={'type':'text', 'pattern':'.{8}', 'name': 'dni', 'placeholder': '12345678', 'title': 'Este campo debe tener 8 dígitos numéricos'}))
