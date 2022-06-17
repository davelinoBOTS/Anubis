from enum import Enum
from django.utils.translation import gettext_lazy as _


class TypeAddress(Enum):
    HOME = _("Home")
    WORK = _("Work")
    FAMILY = _("Family")
    OUTHERS = _("Outhers")

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value(cls, member):
        return cls[member].value


class TypePhone(Enum):
    HOME = _("Home")
    WORK = _("Work")
    FAMILY = _("Family")
    MOBILE = _("Mobile")
    FAX = _("Fax")
    OUTHERS = _("Outhers")

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value(cls, member):
        return cls[member].value
