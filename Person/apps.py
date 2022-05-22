from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PersonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Person'
    verbose_name = _("M001")

    def __init__(self, app_name, app_module):
        super(PersonConfig, self).__init__(app_name, app_module)
        self.icon = "fa-solid fa-users"
