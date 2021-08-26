from django.apps import AppConfig

class YoutubeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtube'

    # def ready(self):
    #     from .updater import start
    #     start()