import json

from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from regions.models import Region


class Command(BaseCommand):
    help = 'Populates the database with countries'

    def add_arguments(self, parser):
        parser.add_argument('--json', action="store_true", help='Output the data in JSON format')

    def handle(self, *args, **options):
        out_file = '%s/data/regions.'

        if options['json']:
            out_file += 'json'
        else:
            out_file += 'csv'

        out_file = out_file % settings.ROOT_DIR

        with open(out_file, 'w+') as file:
            regions = Region.objects.all()

            if options['json']:
                country_json = serializers.serialize('json', regions)
            else:
                for region in regions:
                    print('%s,%s,%s' % (region.name,
                                        region.code,
                                        region.country.alpha_2_code), file=file)