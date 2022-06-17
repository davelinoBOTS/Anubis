from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRPostalCodeField

from Basic.enums import TypeAddress, TypePhone


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


class Country(EntityBasic):
    codeIBGE = models.CharField(
        verbose_name=_("Verbose Code IBGE"),
        unique=True,
        null=False,
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3)]
    )
    name = models.CharField(
        verbose_name=_("Verbose Name"),
        unique=True,
        null=False,
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200)]
    )
    acronym = models.CharField(
        verbose_name=_("Verbose Acronym"),
        unique=True,
        null=False,
        max_length=3,
        validators=[MinLengthValidator(3), MaxLengthValidator(3)]
    )
    nationality = models.CharField(
        verbose_name=_("Verbose Nationality"),
        null=True,
        blank=True,
        max_length=200,
        validators=[MaxLengthValidator(200)]
    )

    class Meta:
        ordering = ["name", "codeIBGE", "acronym"]
        verbose_name = _("Verbose Country")
        verbose_name_plural = _("Verbose Country Plural")

    def __str__(self):
        return '{0}-{1} [IBGE: {2}]'.format(self.name, self.acronym, self.codeIBGE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        if self.acronym is not None:
            self.acronym = self.acronym.upper()

        return EntityBasic.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                update_fields=update_fields)


class State(EntityBasic):
    codeIBGE = models.CharField(
        verbose_name=_("Verbose Code IBGE"),
        unique=True,
        null=False,
        max_length=2,
        validators=[MinLengthValidator(2), MaxLengthValidator(2)]
    )
    name = models.CharField(
        verbose_name=_("Verbose Name"),
        null=False,
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200)]
    )
    acronym = models.CharField(
        verbose_name=_("Verbose Acronym"),
        null=False,
        max_length=2,
        validators=[MinLengthValidator(2), MaxLengthValidator(2)]
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose Country"),
        null=False
    )

    class Meta:
        ordering = ["name", "codeIBGE", "acronym"]
        verbose_name = _("Verbose State")
        verbose_name_plural = _("Verbose State Plural")

        unique_together = (
            ('name', 'country'),
            ('acronym', 'country')
        )

    def __str__(self):
        return '{0}-{1}-{2} [IBGE: {3}]'.format(self.name, self.acronym, self.country.acronym, self.codeIBGE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        if self.acronym is not None:
            self.acronym = self.acronym.upper()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class Territory(EntityBasic):
    name = models.CharField(
        verbose_name=_("Verbose Name"),
        null=False,
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200)]
    )
    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose State"),
        null=False
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Verbose Territory")
        verbose_name_plural = _("Verbose Territory Plural")

        unique_together = (
            ('name', 'state')
        )

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.name, self.state.acronym, self.state.country.acronym)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class City(EntityBasic):
    codeIBGE = models.CharField(
        verbose_name=_("Verbose Code IBGE"),
        unique=True,
        null=False,
        max_length=7,
        validators=[MinLengthValidator(7), MaxLengthValidator(7)]
    )
    name = models.CharField(
        verbose_name=_("Verbose Name"),
        null=False,
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200)]
    )
    isCapital = models.BooleanField(
        verbose_name=_("Verbose Is Capital"),
        null=False,
        default=False
    )
    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose State"),
        null=False
    )
    territory = models.ForeignKey(
        Territory,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose Territory"),
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["name", "codeIBGE"]
        verbose_name = _("Verbose City")
        verbose_name_plural = _("Verbose City Plural")

        unique_together = (
            ('name', 'state')
        )

    def __str__(self):
        return '{0}-{1} [IBGE: {2}]'.format(self.name, self.state.acronym, self.codeIBGE)

    def clean(self):
        if self.isCapital and City.objects.filter(state=self.state, isCapital=True).count() > 0:
            raise ValidationError(
                {'state': _("This state already has a registered capital")}
            )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class Neighborhood(EntityBasic):
    name = models.CharField(
        verbose_name=_("Verbose Name"),
        null=False,
        max_length=200,
        validators=[MinLengthValidator(3), MaxLengthValidator(200)]
    )
    zone = models.CharField(
        verbose_name=_("Verbose Zone"),
        null=True,
        blank=True,
        max_length=100,
        validators=[MaxLengthValidator(100)]
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose City"),
        null=False
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Verbose Neighborhood")
        verbose_name_plural = _("Verbose Neighborhood Plural")

        unique_together = (
            ('name', 'city')
        )

    def __str__(self):
        return '{0}-{1}-{2}-{3}'.format(self.name, self.city.name, self.city.state.acronym,
                                        self.city.state.country.acronym)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class Address(EntityBasic):
    publicPlace = models.CharField(
        verbose_name=_("Verbose Public Place"),
        null=False,
        max_length=255,
        validators=[MinLengthValidator(5), MaxLengthValidator(255)]
    )
    number = models.CharField(
        verbose_name=_("Verbose Number"),
        null=True,
        blank=True,
        max_length=5,
        validators=[MaxLengthValidator(5)]
    )
    complement = models.CharField(
        verbose_name=_("Verbose Complement"),
        null=True,
        blank=True,
        max_length=255,
        validators=[MaxLengthValidator(255)]
    )
    referencePoint = models.TextField(
        verbose_name=_("Verbose Reference Point"),
        null=True,
        blank=True
    )
    zipCode = BRPostalCodeField(
        verbose_name=_("Verbose Zip Code"),
        null=False
    )
    typeAddress = models.CharField(
        verbose_name=_("Verbose Type Address"),
        null=False,
        max_length=100,
        choices=[(tag.name, tag.value) for tag in TypeAddress]
    )
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.PROTECT,
        verbose_name=_("Verbose Neighborhood"),
        null=False
    )

    class Meta:
        ordering = ["publicPlace", "zipCode", "typeAddress"]
        verbose_name = _("Verbose Address")
        verbose_name_plural = _("Verbose Address Plural")

    def __str__(self):
        NUMBER = 'S/N'

        if self.number != '':
            NUMBER = self.number

        return '{0}, {1} - {2}'.format(self.publicPlace, NUMBER, self.neighborhood)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)


class Phone(EntityBasic):
    ddd = models.CharField(
        verbose_name=_("Verbose DDD"),
        null=False,
        max_length=2,
        validators=[MinLengthValidator(2), MaxLengthValidator(2)]
    )
    number = models.CharField(
        verbose_name=_("Verbose Number"),
        null=False,
        max_length=10,
        validators=[MinLengthValidator(9), MaxLengthValidator(10)]
    )
    extension = models.CharField(
        verbose_name=_("Verbose Extension"),
        null=True,
        blank=True,
        max_length=5,
        validators=[MaxLengthValidator(5)]
    )
    contact = models.CharField(
        verbose_name=_("Verbose Contact"),
        null=True,
        blank=True,
        max_length=100,
        validators=[MaxLengthValidator(100)]
    )
    typePhone = models.CharField(
        verbose_name=_("Verbose Type Phone"),
        null=False,
        max_length=100,
        choices=[(tag.name, tag.value) for tag in TypePhone]
    )

    class Meta:
        ordering = ["ddd"]
        verbose_name = _("Verbose Phone")
        verbose_name_plural = _("Verbose Phone Plural")

    def __str__(self):
        return '({0}) {1}'.format(self.ddd, self.number)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updateDate = timezone.now()

        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using,
                                 update_fields=update_fields)
