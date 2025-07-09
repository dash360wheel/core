from django.apps import AppConfig


class CrudactionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crudActions'

def ready(self):
    from . import signals
