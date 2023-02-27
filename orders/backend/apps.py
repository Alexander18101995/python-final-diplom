from django.apps import AppConfig
from backend.signals import password_reset_token_created,new_user_registered_signal,new_order_signal

class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        password_reset_token_created
        new_user_registered_signal
        new_order_signal

