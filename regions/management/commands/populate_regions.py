import csv
import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from countries.models import Country
from regions.models import Region


class Command(BaseCommand):
    help = 'Populates the database with regions'

    def handle(self, *args, **options):
        in_file = '%s/data/regions.csv' % settings.ROOT_DIR

        with open(in_file, 'r') as file:
            csvReader = csv.reader(file)

            NAME = 0
            CODE = 1
            COUNTRY = 2

            for row in csvReader:
                try:
                    country = Country.objects.get(alpha_2_code__iexact=row[COUNTRY])
                except Country.DoesNotExist:
                    print('Country doesn\'t exist: %s' % row[COUNTRY])
                    continue

                region, created = Region.objects.get_or_create(name=row[NAME], code=row[CODE], country=country)