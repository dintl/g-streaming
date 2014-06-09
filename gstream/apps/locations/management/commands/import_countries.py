import os
import sys
import csv
import codecs

from django.db import transaction
from django.conf import settings
from django.core.management.base import BaseCommand
from gstream.apps.locations.models import Country, Continent

class Command(BaseCommand):
    args = '<limit (optional)>'
    help = 'Imports from the old data.TreeEquation model to the new normalized structure'

    def handle(self,*args, **options):

        #First make sure we import all of the countries
        country_data = self.load_countries_csv()

        continents = {
            'AF' : 'Africa',
            'AN' : 'Antatica',
            'AS' : 'Asia',
            'EU' : 'Europe',
            'NA' : 'North America',
            'OC' : 'Oceania',
            'SA' : 'South America'
        }

        for key in continents.keys():
            name = continents[key]
            continents[key] = Continent.objects.create(code=key, name=name)

        for cd_row in country_data:
            Country.objects.create(
                common_name=cd_row['ISOen_name'],
                formal_name=cd_row['ISOen_proper'],
                common_name_fr=cd_row['ISOfr_name'],
                formal_name_fr=cd_row['ISOfr_proper'],
                continent=continents[cd_row['continent']],
                iso3166a2=cd_row['ISO3166A2'],
                iso3166a3=cd_row['ISO3166A3'],
                iso3166n3=cd_row['ISO3166N3'],
                centroid_latitude = cd_row['latitude'],
                centroid_longitude = cd_row['longitude'] 
            )
