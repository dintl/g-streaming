from django.contrib import admin
from gstream.apps.locations.models import Continent, Country

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'common_name_fr', 'iso3166a2', 'continent', 'centroid_longitude', 'centroid_latitude')
    list_filter  = ('continent', )

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)

