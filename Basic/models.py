from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class EntityBasic(models.Model):
    id = models.AutoField(
        verbose_name=_("Verbose ID"),
        primary_key=True,
        unique=True,
        null=False
    )
    registrationDate = models.DateTimeField(
        verbose_name=_("Verbose Registration Date"),
        null=False,
        default=timezone.now
    )
    updateDate = models.DateTimeField(
        verbose_name=_("Verbose Update Date"),
        null=False,
        default=timezone.now
    )
    isActive = models.BooleanField(
        verbose_name=_("Verbose Is Active"),
        null=False,
        default=True
    )

    class Meta:
        abstract = True
