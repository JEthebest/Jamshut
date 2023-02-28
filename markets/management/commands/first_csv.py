import csv

from django.core.management.base import BaseCommand

from ...models import Location

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='path to csv file', )

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        file = open(path)
        csvreader = csv.reader(file)
        locations = []
        for row in csvreader:
            locations.append(Location(location_name=row[0]))

        Location.objects.bulk_create(locations)