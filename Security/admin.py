from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from Security.models import PermissionGroup


class PermissionGroupAdmin(admin.ModelAdmin):

    search_fields = ["name", "description"]

    list_display = ["name", "isActive"]
    list_filter = ["isActive"]

    def get_queryset(self, request):
        queryset = PermissionGroup.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["name", "permissions", "description", "isActive", "registrationDate",
                                       "updateDate"]})
                          ]

        form = super(PermissionGroupAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(PermissionGroup, PermissionGroupAdmin)

admin.site.unregister(Group)
