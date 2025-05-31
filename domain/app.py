import threading

from django.apps import AppConfig


class DomainConfig(AppConfig):
    name = 'domain'
    models_module = 'domain.models'