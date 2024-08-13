from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django_recaptcha.fields import ReCaptchaField, ReCaptchaV2Checkbox
from django.forms import ModelForm

# Create your models here.
#class Curso:
    #programa = models.CharField(max_length=255)
    #nombreCurso = models.CharField(max_length=160)
    #nota = models.CharField(max_length=5)
    #horas = models.CharField(max_length=2)

class Persona(forms.Form):
    apellido = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'type':'text', 'pattern':'[A-ZÑ]+', 'name': 'apellido', 'placeholder': 'PEREZ', 'title': 'Este campo debe tener letras mayúsculas'}))
    dni = forms.CharField(required=True, max_length=11, widget=forms.TextInput(attrs={'type':'text', 'pattern':'.{8}', 'name': 'dni', 'placeholder': '12345678', 'title': 'Este campo debe tener 8 dígitos numéricos'}))
    recaptcha = ReCaptchaField(required=True, widget=ReCaptchaV2Checkbox(), public_key='6Lcjxg4qAAAAAM2PCbF_cI6LElkbajJjozp3pdaM', private_key='6Lcjxg4qAAAAALX_2GA1ujoolSi06sNEFKR3O33A')
