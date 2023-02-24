from django.apps import AppConfig
from backend.signals import create_profile

class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        create_profile


