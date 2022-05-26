from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from Basic.models import Country, State, Territory, City, Neighborhood


class CountryAdmin(admin.ModelAdmin):
    search_fields = ["codeIBGE", "name", "acronym"]

    list_display = ["codeIBGE", "name", "acronym", "nationality", "isActive"]
    list_filter = ["isActive"]

    def get_queryset(self, request):
        queryset = Country.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["codeIBGE", "name", "acronym", "nationality", "isActive",
                                       "registrationDate", "updateDate"]}),
                          ]

        form = super(CountryAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    search_fields = ["codeIBGE", "name", "acronym", "country__name", "country__acronym", "country__nationality"]

    list_display = ["codeIBGE", "name", "acronym", "country", "isActive"]
    list_filter = ["isActive"]

    def get_queryset(self, request):
        queryset = State.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["codeIBGE", "name", "acronym", "country", "isActive",
                                       "registrationDate", "updateDate"]}),
                          ]

        form = super(StateAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(State, StateAdmin)


class TerritoryAdmin(admin.ModelAdmin):
    search_fields = ["name", "state__name", "state__acronym"]

    list_display = ["name", "state", "isActive"]
    list_filter = ["isActive"]

    def get_queryset(self, request):
        queryset = Territory.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["name", "state", "isActive",
                                       "registrationDate", "updateDate"]}),
                          ]

        form = super(TerritoryAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(Territory, TerritoryAdmin)


class CityAdmin(admin.ModelAdmin):
    search_fields = ["codeIBGE", "name", "state__name", "state__acronym", "territory__name"]

    list_display = ["codeIBGE", "name", "territory", "state", "isCapital", "isActive"]
    list_filter = ["isActive", "isCapital"]

    def get_queryset(self, request):
        queryset = City.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["codeIBGE", "name", "territory", "state", "isCapital", "isActive",
                                       "registrationDate", "updateDate"]}),
                          ]

        form = super(CityAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(City, CityAdmin)


class NeighborhoodAdmin(admin.ModelAdmin):
    search_fields = ["name",  "zone", "city__name"]

    list_display = ["name", "zone", "city", "isActive"]
    list_filter = ["isActive"]

    def get_queryset(self, request):
        queryset = Neighborhood.objects.all()

        return queryset

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.readonly_fields = ["registrationDate", "updateDate"]
        else:
            self.readonly_fields = ["registrationDate", "updateDate"]

        self.fieldsets = [(_("Fieldset General"),
                           {"fields": ["name", "zone", "city", "isActive",
                                       "registrationDate", "updateDate"]}),
                          ]

        form = super(NeighborhoodAdmin, self).get_form(request, obj, **kwargs)

        return form


admin.site.register(Neighborhood, NeighborhoodAdmin)
