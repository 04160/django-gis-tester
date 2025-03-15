from django.core.management.base import BaseCommand, CommandError
from coordinates.models import Location
import random
from datetime import datetime


class Command(BaseCommand):
    help = 'Generate test data for coordinates'

    def add_arguments(self, parser):
        parser.add_argument("coord_count", nargs="+", type=int)

    def handle(self, *args, **options):
        oldLocationCount = Location.objects.count()

        for count in range(options['coord_count'][0]):
            lat, lng = self._calculateCoords()
            timestamp = datetime.now().strftime("%H%M%S-%d%m%Y")
            Location.objects.create(
                name=f"generated_{count + 1}_{timestamp}",
                lat=lat,
                lng=lng
            )

        newLocationCount = Location.objects.count()
        print(f"Old location count: {oldLocationCount}. New count: {newLocationCount}")

    def _calculateCoords(str: str) -> tuple[float, float]:
        lat = 56.8801729 + (random.randint(-200, 200) / 100)
        lng = 24.6057484 + (random.randint(-200, 200) / 100)

        return lat, lng
