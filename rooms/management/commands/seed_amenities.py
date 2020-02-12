from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):

    help = "This command creates amenities"

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many..."
        )
    """

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Wifi",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Private bathroom",        
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))