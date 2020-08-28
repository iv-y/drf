from django.conf import settings
from django.apps import apps

def get_user_model():
    app_name, model_name = settings.AUTH_USER_MODEL.split('.')
    return apps.get_app_config(app_name).get_model(model_name, require_ready = True)