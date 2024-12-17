from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """This runs when the app is ready, not when imported."""
        if not firebase_admin._apps:  # Check if the app is already initialized
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
