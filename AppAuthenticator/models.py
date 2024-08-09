from django import forms
from django.db import models
from django_recaptcha.fields import ReCaptchaField

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=160)

class Formulario(forms.Form):
    apellido = forms.CharField(max_length=30, required=True, error_messages={'required': 'El apellido debe contener solo letras mayúsculas y espacios.'})
    dni = forms.CharField(max_length=11, required=True, error_messages={'required':'El DNI debe tener exactamente 8 dígitos numéricos.'})
    recaptcha = ReCaptchaField(
        public_key='6Lcjxg4qAAAAAM2PCbF_cI6LElkbajJjozp3pdaM',
        private_key='6Lcjxg4qAAAAALX_2GA1ujoolSi06sNEFKR3O33A',
        error_messages={'required': 'Debes seleccionar el captcha para poder conocer el resultado de la búsqueda que realizó'}
    )

class CursoEncontrado(models.Model):
    programa = models.CharField(max_length=255)
    nombre = models.CharField(max_length=160)
    nota = models.CharField(max_length=5)
    horas = models.CharField(max_length=2)
