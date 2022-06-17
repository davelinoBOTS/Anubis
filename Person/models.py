import re

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField

from Anubis.codes_get import get_code_automatic
from Anubis.utils import UserManager
from Anubis.validators import validate_images_extension
from Basic.models import EntityBasic, Phone, Address
from Person.enums import Sex


class Person(EntityBasic):
    email = models.EmailField(
        verbose_name=_("Verbose Email"),
        null=True,
        blank=True
    )
    photo = models.ImageField(
        verbose_name=_("Verbose Photo"),
        null=True,
        blank=True,
        upload_to="admin/person/photos/",
        validators=[validate_images_extension]
    )

    class Meta:
        abstract = True


class PhysicalPerson(Person):
    fullName = models.CharField(
        verbose_name=_("Verbose Full Name"),
        null=False,
        max_length=255,
        validators=[MinLengthValidator(5), MaxLengthValidator(255)]
    )
    cpf = BRCPFField(
        verbose_name=_("Verbose CPF"),
        null=False
    )
    rg = models.CharField(
        verbose_name=_("Verbose RG"),
        null=True,
        blank=True,
        max_length=20,
        validators=[MaxLengthValidator(20)]
    )
    birthDate = models.DateField(
        verbose_name=_("Verbose Date Birth"),
        null=True,
        blank=True
    )
    sex = models.CharField(
        verbose_name=_("Verbose Sex"),
        null=True,
        blank=True,
        max_length=100,
        choices=Sex.choices()
    )

    class Meta:
        ordering = ["fullName", "cpf", "sex"]
        verbose_name = _("Verbose Physical Person")
        verbose_name_plural = _("Verbose Physical Person Plural")

    def __str__(self):
        return "[{0}] {1}".format(self.cpf, self.fullName)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class PhysicalPersonPhone(Phone):
    physicalPerson = models.ForeignKey(
        PhysicalPerson,
        on_delete=models.CASCADE,
        verbose_name=_("Verbose Physical Person"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Verbose Phone")
        verbose_name_plural = _("Verbose Phone Plural")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class PhysicalPersonAddress(Address):
    physicalPerson = models.ForeignKey(
        PhysicalPerson,
        on_delete=models.CASCADE,
        verbose_name=_("Verbose Physical Person"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Verbose Address")
        verbose_name_plural = _("Verbose Address Plural")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class SystemUser(AbstractBaseUser, PermissionsMixin, EntityBasic):
    code = models.CharField(
        verbose_name=_("Verbose Code"),
        unique=True,
        null=False,
        max_length=17,
        validators=[MinLengthValidator(17), MaxLengthValidator(17)]
    )
    username = models.CharField(
        _("Verbose Username"),
        null=False,
        max_length=15,
        help_text=_("Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=([validators.RegexValidator(re.compile("^[\w.@+-]+$"), _("Valid user."), _("invalid"))])
    )
    email = models.EmailField(
        _("Verbose Email"),
        blank=True
    )
    first_name = models.CharField(
        _("Verbose First Name"),
        max_length=30
    )
    last_name = models.CharField(
        _("Verbose Last Name"),
        max_length=30
    )
    is_staff = models.BooleanField(
        _("Verbose Staff Status"),
        null=False,
        default=False,
        help_text=_("Designates whether the user can log into this admin site.")
    )
    is_superuser = models.BooleanField(
        _("Verbose Superuser Status"),
        default=False,
        help_text=_("Designates that this user has all permissions.")
    )
    is_active = models.BooleanField(
        _("Verbose Is Active"),
        null=False,
        default=True,
        help_text=_("Designates whether this user should be treated as active. Uncheck this instead of deleting "
                    "accounts.")
    )
    date_joined = models.DateTimeField(
        _("Verbose Date Joined"),
        default=timezone.now
    )
    physicalPerson = models.ForeignKey(
        PhysicalPerson,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose Physical Person"),
        null=True,
        blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = UserManager()

    class Meta:
        ordering = ["code", "username", "first_name", "last_name"]
        verbose_name = _("Verbose System User")
        verbose_name_plural = _("Verbose System User Plural")

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)

        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        if self.code == "":
            self.code = get_code_automatic(SystemUser.objects.last(), "SystemUser")

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)
