import json

from django.conf import settings
from django.core import serializers
from django.core.management.base import BaseCommand, CommandError
from countries.models import Continent, Country


class Command(BaseCommand):
    help = 'Populates the database with countries'

    def add_arguments(self, parser):
        parser.add_argument('--json', action="store_true", help='Output the data in JSON format')

    def handle(self, *args, **options):
        out_file = '%s/data/countries.'

        if options['json']:
            out_file += 'json'
        else:
            out_file += 'csv'

        out_file = out_file % settings.ROOT_DIR

        print(out_file)
        with open(out_file, 'w+') as file:
            countries = Country.objects.all()

            if options['json']:
                country_json = serializers.serialize('json', countries)
                print(country_json)
                print(json.dumps(country_json, indent=4, sort_keys=False), file=file)
            else:
                for country in countries:
                    print('%s,%s,%s,%s,%s,%s,%s' % (country.name,
                                                    country.alpha_2_code,
                                                    country.alpha_3_code,
                                                    country.continent.code,
                                                    country.calling_code,
                                                    country.capital_city,
                                                    country.native_name), file=file)