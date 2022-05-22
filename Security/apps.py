from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Security'
    verbose_name = _("M002")

    def __init__(self, app_name, app_module):
        super(SecurityConfig, self).__init__(app_name, app_module)
        self.icon = "fa-solid fa-building-shield"
