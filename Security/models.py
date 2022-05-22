from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from Basic.models import EntityBasic


class PermissionGroup(Group, EntityBasic):
    description = models.TextField(
        verbose_name=_("Verbose Description"),
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Verbose Permission Group")
        verbose_name_plural = _("Verbose Permission Group Plural")

    def __str__(self):
        return "{0}".format(self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)
