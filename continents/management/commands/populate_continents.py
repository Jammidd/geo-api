import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from countries.models import Continent


class Command(BaseCommand):
    help = 'Populates the database with continents'

    def handle(self, *args, **options):
        in_file = '%s/data/continents.csv' % settings.ROOT_DIR

        with open(in_file, 'r') as file:
            csvReader = csv.reader(file)

            for row in csvReader:
                continent, created = Continent.objects.get_or_create(code=row[0], name=row[1])

