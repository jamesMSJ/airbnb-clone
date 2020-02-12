from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):

    help = "This command creates facilities"

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many..."
        )
    """

    def handle(self, *args, **options):
        facilities = [
            "Washer",
            "Dryer",
            "Breakfast",
            "Indoor fireplace",
            "Crib",
            "High chair",
            "Self check-in",
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("facilities created!"))