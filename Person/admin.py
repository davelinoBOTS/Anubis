from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from Person.models import PhysicalPerson, SystemUser


class PhysicalPersonAdmin(admin.ModelAdmin):
    search_fields = ["fullName", "cpf", "rg", "birthDate", "sex"]

    list_display = ["fullName", "sex", "cpf", "rg", "birthDate", "isActive"]
    list_filter = ["isActive"]

    def get_queryset(self, request):
        queryset = PhysicalPerson.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["fullName", "photo", "cpf", "rg", "email", "sex", "birthDate", "isActive",
                                       "registrationDate", "updateDate"]}),
                          ]

        form = super(PhysicalPersonAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(PhysicalPerson, PhysicalPersonAdmin)


class SystemUserAdmin(admin.ModelAdmin):

    search_fields = ["code", "username"]

    list_display = ["code", "username", "is_superuser", "is_active"]
    list_filter = ["is_active", "is_superuser", "is_staff"]

    def get_queryset(self, request):
        queryset = SystemUser.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["password", "registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["code", "physicalPerson", "first_name", "last_name", "email"]}),
                          (_("Fieldset Access"),
                           {"fields": ["username", "password"]}),
                          (_("Fieldset Permissions"),
                           {"fields": ["groups", "user_permissions", "is_staff", "is_superuser", "is_active",
                                       "isActive", "registrationDate", "updateDate"]}),
                          ]

        form = super(SystemUserAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(SystemUser, SystemUserAdmin)
