import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from countries.models import Continent, Country


class Command(BaseCommand):
    help = 'Populates the database with countries'

    def handle(self, *args, **options):
        in_file = '%s/data/countries.csv' % settings.ROOT_DIR

        with open(in_file, 'r') as file:
            csvReader = csv.reader(file)

            NAME = 0
            ALPHA2 = 1
            ALPHA3 = 2
            CONTINENT = 3
            CALLING = 4
            CAPITAL = 5
            NATIVE = 6

            for row in csvReader:
                try:
                    continent = Continent.objects.get(code=row[CONTINENT])
                except Continent.DoesNotExist:
                    print('Invalid continent: %s' % row[NAME])
                    continue

                country_data = {
                    'name': row[NAME],
                    'alpha_2_code': row[ALPHA2],
                    'alpha_3_code': row[ALPHA3],
                    'continent': continent,
                    'calling_code': row[CALLING],
                    'capital_city': row[CAPITAL],
                    'native_name': row[NATIVE]
                }

                try:
                    country, created = Country.objects.get_or_create(**country_data)
                except Exception as ex:
                    print('Error inserting: %s' % country_data['name'])
                    continue