from django.apps import AppConfig
from django.core.checks import Tags, register

from django_recaptcha.checks import recaptcha_key_check

class AppauthenticatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppAuthenticator'

    def ready(self):
        register(recaptcha_key_check, Tags.security)
