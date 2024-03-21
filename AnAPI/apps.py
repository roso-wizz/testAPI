from django.apps import AppConfig


class AnapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AnAPI'

    def ready(self):
        import AnAPI.signalz
