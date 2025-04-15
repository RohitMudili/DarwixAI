from django.apps import AppConfig

class TitlesuggestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'titlesuggest'
    
    def ready(self):
        # This ensures Django is fully loaded before we use any models
        pass