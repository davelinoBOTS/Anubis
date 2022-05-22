from enum import Enum
from django.utils.translation import gettext_lazy as _


class Sex(Enum):
    MALE = _("MALE")
    FEMALE = _("FEMALE")

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value(cls, member):
        return cls[member].value
