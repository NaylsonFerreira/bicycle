from django.contrib.admin.apps import AdminConfig as _AdminConfig
from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'


class AdminConfig(_AdminConfig):
    default_site = 'api_app.admin.AdminSite'
