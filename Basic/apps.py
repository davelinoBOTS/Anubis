from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BasicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Basic'
    verbose_name = _("M000")

    def __init__(self, app_name, app_module):
        super(BasicConfig, self).__init__(app_name, app_module)
        self.icon = "fa-solid fa-suitcase"
